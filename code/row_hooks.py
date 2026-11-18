"""《脈經》（99k3i35yww）Step3 行切分书级钩子：覆盖 cv `impl/keben/row_hooks`。

只给 `jiazhu_heads`：按本书的噪点段门槛补认雙行小注段。

缘由（2026-11-18，MJ 第 1 册切分优化）：缺省 `jiazhu_split.link_runs` 用段中位「两侧较小最大连通体」< 500px
整段否决（噪点段），是殿本小字标定的。本书刻本小字笔画细，单字最大连通体多在 200–600px（第 1 册 p13 c5 段中位
486、c4 490、c7 408），整段真夹注被当噪点否决，两行小字挤进整宽格。第 1 册全册试过门槛 100／200 结果逐位相同
（12 列补认夹注、看图无误判），取 200。

做法：照缺省 `link_runs` 原样重连一遍（桥接、对齐容差、段长都不变），只把否决门槛换成 `CC_MIN`，
返回缺省没认下的段（不改输入）。要在册配置开 `row_segment.jiazhu_single_head: true` 才调（cv 的开关名沿用全唐文）。
cv 只许 import `open_guji_cv.seg`／`book_api`，所以常量与逻辑照抄 cv `impl/keben/jiazhu_split.link_runs`（cv 78c29c0b）。
"""
from __future__ import annotations

CC_MIN = 200          # 本书噪点段否决门槛（缺省 500）
ALIGN = 8             # 同 cv jiazhu_split.ALIGN
ALIGN_PAIR = 16       # 同 cv jiazhu_split.ALIGN_PAIR
MIN_RUN = 2           # 同 cv jiazhu_split.MIN_RUN


def _link_runs(entries, cc_min: float) -> dict[int, float]:
    ents = sorted(entries)
    measured = {i: c for i, c in ents if c is not None}
    cmap: dict[int, float] = {i: c[0] for i, c in measured.items()}
    smap: dict[int, float] = {i: c[1] for i, c in measured.items()}
    for i, c in ents:
        if c is not None:
            continue
        a, b = measured.get(i - 1), measured.get(i + 1)
        if a is not None and b is not None and abs(a[0] - b[0]) <= ALIGN:
            cmap[i] = (a[0] + b[0]) / 2
    out: dict[int, float] = {}

    def _commit(run: list[int]) -> None:
        if len(run) < MIN_RUN:
            return
        strengths = sorted(smap[j] for j in run if j in smap)
        if not strengths or strengths[len(strengths) // 2] < cc_min:
            return
        out.update({j: cmap[j] for j in run})

    run: list[int] = []
    prev_i = None
    for i in sorted(cmap):
        align = ALIGN if len(run) >= 2 else ALIGN_PAIR
        ok = (prev_i is not None and i == prev_i + 1
              and abs(cmap[i] - cmap[prev_i]) <= align)
        if ok:
            run.append(i)
        else:
            _commit(run)
            run = [i]
        prev_i = i
    _commit(run)
    return out


SEAM_SPAN_MIN = 0.75     # 收边格墨迹跨度/列距下限（同 cv jiazhu_split.SPAN_T：两行小字合起来占满列宽）
SEAM_TOL = 14            # 收边格的缝离邻格缝中心的容差（px）
SEAM_BAND = 3            # 缝带半宽（px）
SEAM_INK_FRAC = 0.03     # 缝带里墨行占比上限：缝上几乎没墨才算两行
SEAM_SIDE_MIN = 60       # 缝两侧各自的墨下限（px）


def _seam_ok(patch, cx: float, ink_threshold: int, ruler: float) -> float | None:
    """这一格在 cx 附近有没有一条几乎无墨的竖缝、两侧都有字：有就返回缝中心（局部坐标）。"""
    import numpy as np
    b = patch < ink_threshold
    xp = b.sum(axis=0)
    ink = np.flatnonzero(xp > 0)
    if len(ink) < 10 or (ink[-1] - ink[0] + 1) / float(ruler) < SEAM_SPAN_MIN:
        return None
    h = b.shape[0]
    best = None
    lo, hi = int(cx - SEAM_TOL), int(cx + SEAM_TOL)
    for x in range(max(SEAM_BAND, lo), min(b.shape[1] - SEAM_BAND, hi + 1)):
        rows = b[:, x - SEAM_BAND:x + SEAM_BAND + 1].any(axis=1).mean()
        if best is None or rows < best[0] or (rows == best[0] and abs(x - cx) < abs(best[1] - cx)):
            best = (rows, x)
    if best is None or best[0] > SEAM_INK_FRAC:
        return None
    x = best[1]
    if b[:, :max(0, x - SEAM_BAND)].sum() < SEAM_SIDE_MIN or b[:, x + SEAM_BAND + 1:].sum() < SEAM_SIDE_MIN:
        return None
    return float(x)


def _grow(runs: dict[int, float], patches, eligible, ink_threshold, ruler) -> dict[int, float]:
    """段端收边：已认的段上下紧邻的格，在段缝位附近有干净竖缝就并进来，连着往外长（段首「得一」「索一」这类
    判据量不出缝的行）。只从已成段的格长：单格量出缝的格多是左右结构的正文字（細、謂、射），从它长会把正文劈开
    （第 1 册试过，13:10、16:1、22:12 误拆）。"""
    seeds = dict(runs)
    out: dict[int, float] = {}
    for p0, cx0 in sorted(seeds.items()):
        for step in (-1, 1):
            p, cx = p0 + step, cx0
            while p in patches and p in eligible and p not in seeds and p not in out:
                got = _seam_ok(patches[p], cx, ink_threshold, ruler)
                if got is None:
                    break
                out[p] = got
                cx = got
                p += step
    return out


def jiazhu_heads(entries, runs, patches, eligible, ink_threshold, ruler) -> dict[int, float]:
    """缺省门槛没认下、本书门槛认下的夹注段，加段端收边 → {pos: 缝中心}（只返回新增的格）。"""
    linked = _link_runs(entries, CC_MIN)
    allruns = {**linked, **runs}
    grown = _grow(allruns, patches, eligible, ink_threshold, ruler)
    new = {**linked, **grown}
    return {p: cx for p, cx in new.items() if p not in runs}


grid_adjust = None
half_a_left = None
jiazhu_pair_ok = None
edge_frame_only = None

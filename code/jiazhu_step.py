"""《脈經》雙行小注按小字字距分行（书级钩子 `jiazhu_step.row_split`，cv #1713；GUJI-774）。其余接口照缺省。

本书多数雙行小注小字与大字同距（一段每行字数＝段占的大字格数），照旧切；少数密排小注（01 p13 c5／c8／c11）
小字只有大字格高的 0.6–0.8，一段每行字数多于大字格数。分辨靠这一行墨投影的自相关：同距小注在 1 个大字格高处
自相关明显（≥ AC_SAME），密排小注那里几乎为零、峰落在 0.55–0.9 格高。只有后者才按峰的位置定小字字距、
在其 ±1 字里挑切线压墨＋行高偏离最小的字数（A22 参考实现的做法），且字数要多于大字格数才接。
段内大连通块高度中位数 ≥ 0.8 格高的是被误认成小注的大字（A22 建议的护栏），不接。
"""
from __future__ import annotations

import numpy as np
from scipy import ndimage

from open_guji_cv.seg.seam import fit_row_cuts

MIN_LEN = 2.5           # 段短于这么多格高不接（只两格的段自相关看不出字距；01 p10 c2 列首「則可」2.1 格被多切一字）
BIG_CC = 0.8            # 段内大连通块（面积 ≥ CC_MIN_AREA）高度中位数到这么多格高＝其实是大字（01 p10 c2 列首「則可」），不另切
CC_MIN_AREA = 200
AC_SAME = 0.12          # 一格高处（0.9–1.1 格）自相关到这么高＝小字与大字同距，不另切
LAG_LO, LAG_HI = 0.55, 0.9   # 密排小字字距的搜索范围（大字格高的倍数）
PITCH_W = 0.6           # 行高离小字字距的罚分


def _autocorr(x):
    x = x - x.mean()
    ac = np.correlate(x, x, "full")[len(x) - 1:]
    return ac / (ac[0] + 1e-9)


def row_split(ink, top, bot, n_grid, period):
    """这一行切几个小字；同距小注或字数不多于大字格数时返回 None（照旧切 n_grid 格）。"""
    t, b = int(round(top)), int(round(bot))
    L = float(b - t)
    if period <= 0 or L < MIN_LEN * period:
        return None
    w = max(1, ink.shape[1])
    rows = ink.sum(axis=1) / float(w)
    seg = ink[t:b]
    lab, n = ndimage.label(seg)
    if n:
        objs = ndimage.find_objects(lab)
        area = np.bincount(lab.ravel())[1:]
        hs = [sl[0].stop - sl[0].start for sl, a in zip(objs, area) if a >= CC_MIN_AREA]
        if hs and float(np.median(hs)) >= BIG_CC * period:
            return None
    ac = _autocorr(rows[t:b].astype(float))
    hi = int(1.1 * period)
    if hi >= len(ac) or float(ac[int(0.9 * period):hi + 1].max()) >= AC_SAME:
        return None
    lo, up = int(LAG_LO * period), int(LAG_HI * period)
    lag = float(lo + int(np.argmax(ac[lo:up + 1])))
    k0 = int(round(L / lag))
    best = None
    for k in range(max(n_grid + 1, k0 - 1), k0 + 2):
        cuts = fit_row_cuts(rows, t, b, k)
        if cuts is None:
            continue
        cut_ink = sum(float(rows[int(round(y))]) for y in cuts[1:-1])
        cost = cut_ink + PITCH_W * (L / k / lag - 1) ** 2 * k
        if best is None or cost < best[0]:
            best = (cost, k, cuts)
    return None if best is None else best[2]


# 其余接口照 cv 缺省（`impl/keben/jiazhu_step`：什么都不做）。书级代码只许 import seg／book_api，这里照抄缺省实现。
def page_note_runs(dz_dir, pins_file, book: str, page: int):
    """本书没有逐列整理本，不做逐步切。"""
    return None


def apply(res, col_gray, content_x, period, specs, ink_threshold: int = 128, reading_order=None):
    return res, []


free_split = None

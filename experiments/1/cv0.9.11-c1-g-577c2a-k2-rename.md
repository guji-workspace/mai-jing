# cv0.9.11-c1-g-577c2a-k2-rename

## 摘要

（存包时没给 `--summary`）

**各步运行**（产物 manifest，最近一轮先后）：

| 步 | 页 | cv | 最后一轮起 → 止（洛杉矶） | 耗时合计 |
|---|---|---|---|---|
| page_survey | 68 | 0.9.7 | 11-26 17:41 → 11-26 18:23 | 0.0 分 |
| invert_detect | 68 | 0.9.7 | 11-26 17:41 → 11-26 18:23 | 0.6 分 |
| border_detect | 68 | 0.9.7 | 11-26 17:56 → 11-26 18:27 | 11.6 分 |
| border_detect_gate | 68 | 0.9.7 | 11-26 17:42 → 11-26 18:28 | 1.6 分 |
| seal_detect | 68 | 0.9.7 | 11-26 17:43 → 11-26 18:28 | 0.6 分 |
| column_warp | 68 | 0.9.7 | 11-26 17:43 → 11-26 18:29 | 2.9 分 |
| column_band | 68 | 0.9.7 | 11-26 17:43 → 11-26 18:29 | 0.2 分 |
| column_end | 68 | 0.9.7 | 11-26 17:43 → 11-26 18:29 | 0.4 分 |
| column_geometry | 68 | 0.9.7 | 11-26 17:43 → 11-26 18:29 | 0.1 分 |
| row_segment | 68 | 0.9.7 | 11-26 17:46 → 11-26 21:48 | 27.8 分 |
| cell_shrink | 68 | 0.9.7 | 11-26 17:46 → 11-26 21:48 | 2.8 分 |
| cut_gate | 68 | 0.9.7 | 11-26 17:46 → 11-26 21:48 | 0.2 分 |
| glyph_match | 68 | 0.9.7 | 11-26 17:52 → 11-26 21:53 | 38.0 分 |
| rare_candidates | 68 | 0.9.7 | 11-26 17:53 → 11-26 21:53 | 1.9 分 |
| align_ref | 68 | 0.9.7 | 11-26 17:53 → 11-26 21:53 | 0.1 分 |
| context_decide | 68 | 0.9.7 | 11-26 17:53 → 11-26 21:53 | 0.1 分 |
| seed_admit | 68 | 0.9.7 | 11-26 17:54 → 11-26 21:54 | 3.9 分 |

## 基本信息

- 册：1
- 存包：2026-11-28T03:01:44Z
- 基线（存包时该册的 main）：—
- 包：`products/99k3i35yww/1/cv0.9.11-c1-g-577c2a-k2-rename`（1176 个文件，5.3 MB）；取回 `guji products pack fetch 1 --label cv0.9.11-c1-g-577c2a-k2-rename --to <目录>`

## 版本

| cv | cv commit | 语料库 | 底库 | 字形库钉号 | 人裁指纹 | 中心库 rev（seed_admit 跑时） |
|---|---|---|---|---|---|---|
| 0.9.11 | 9afc4844cc44 | 1 | 35 | — | h1:3514:577c2a71f4a2797a | 99k3i35yww@main:1571322 |

## 册配置（存包时）

```yaml
id: "1"
aliases: ["01"]          # 11-27 册号位数统一改名，旧名读时换新名
cv_version: "0.9.11"   # 11-28 改名 01→1 后改钉（CV0：0.9.11 含 rename-seal，指纹同 0.9.10）
corpus: 1
title: "脈經 第1冊"
raw_dir: data_full/01
raw_pattern: "{page}.png"
# 叶10、叶20 各两个半叶（cv 页号：叶 L 的 a/b ＝ 2L−2 / 2L−1；1＝书衣，68＝封底）
dev_set: [18, 19, 38, 39]
# 不少页无界行，竖线走网格；列距实测 192（12 列框宽约 2300，2026-11-17 全书量）
column_grid: true
col_pitch: 192
page_kinds:
  roster_cols:
    11: [2]
    37: [2]

  # 林億校定序：参校本（Kanripo）缺这段文字，按无参校本页处理（cv #1702，用户 11-19 定；11-25 随 W1 推库）
  no_ref: ["5-7"]
# 参校本形态（CV0 11-27，Sheldon 定先修参校本 bug）：全书 book_defaults 是 text；林億序（p5–7）Kanripo 本无此段，按页声明 none，
# 与上面 page_kinds.no_ref 同义（align_ref 不再拿 8-gram 硬对、manager 待审归「本就无参照」）。改了这几页从 align_ref 起过期。
reference_profile:
  default: text
  segments:
    - {pages: ["5-7"], kind: none, note: "林億校定序，Kanripo 无"}

# 11-27 用户定脈經开 vline_track；01 册已出 v0.1（main r097b），不重跑，写回关（MJ 告知）。outer_bar 书级仍关
params:
  border_detect:
    vline_track: false
```

## 前后对比

（存包时没给 `--report <diff 目录>`）

## 记事

- 2026-11-28T03:01:47Z ★ 标为 main

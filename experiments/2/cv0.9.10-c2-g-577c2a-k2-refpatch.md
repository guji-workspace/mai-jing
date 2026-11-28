# cv0.9.10-c2-g-577c2a-k2-refpatch

## 摘要

（存包时没给 `--summary`）

**各步运行**（产物 manifest，最近一轮先后）：

| 步 | 页 | cv | 最后一轮起 → 止（洛杉矶） | 耗时合计 |
|---|---|---|---|---|
| page_survey | 78 | 0.9.10 | 11-27 15:10 → 11-27 15:31 | 0.0 分 |
| invert_detect | 78 | 0.9.10 | 11-27 15:10 → 11-27 15:31 | 0.6 分 |
| border_detect | 78 | 0.9.10 | 11-27 15:21 → 11-27 15:35 | 12.1 分 |
| border_detect_gate | 78 | 0.9.10 | 11-27 15:22 → 11-27 15:35 | 1.6 分 |
| seal_detect | 78 | 0.9.10 | 11-27 15:22 → 11-27 15:35 | 0.7 分 |
| column_warp | 78 | 0.9.10 | 11-27 15:22 → 11-27 15:36 | 3.1 分 |
| column_band | 78 | 0.9.10 | 11-27 15:22 → 11-27 15:36 | 0.2 分 |
| column_end | 78 | 0.9.10 | 11-27 15:22 → 11-27 15:37 | 0.4 分 |
| column_geometry | 78 | 0.9.10 | 11-27 15:22 → 11-27 15:37 | 0.1 分 |
| cell_shrink | 78 | 0.9.10 | 11-27 15:24 → 11-27 19:23 | 3.1 分 |
| cut_gate | 78 | 0.9.10 | 11-27 15:24 → 11-27 19:23 | 0.1 分 |
| row_segment | 78 | 0.9.10 | 11-27 19:21 → 11-27 19:31 | 5.2 分 |
| glyph_match | 78 | 0.9.10 | 11-27 19:38 → 11-27 19:56 | 42.8 分 |
| rare_candidates | 78 | 0.9.10 | 11-27 19:56 → 11-27 19:57 | 2.8 分 |
| align_ref | 78 | 0.9.10 | 11-27 19:57 → 11-27 19:57 | 0.1 分 |
| context_decide | 78 | 0.9.10 | 11-27 19:57 → 11-27 19:57 | 0.1 分 |
| seed_admit | 78 | 0.9.10 | 11-27 19:57 → 11-27 19:58 | 3.2 分 |

## 基本信息

- 册：2
- 存包：2026-11-28T04:00:36Z
- 基线（存包时该册的 main）：`cv0.9.10-c1-g-577c2a-k2-first`
- 包：`products/99k3i35yww/2/cv0.9.10-c2-g-577c2a-k2-refpatch`（1345 个文件，7.6 MB）；取回 `guji products pack fetch 2 --label cv0.9.10-c2-g-577c2a-k2-refpatch --to <目录>`

## 版本

| cv | cv commit | 语料库 | 底库 | 字形库钉号 | 人裁指纹 | 中心库 rev（seed_admit 跑时） |
|---|---|---|---|---|---|---|
| 0.9.10 | 1ffb6a61c9b0 | 2 | 35 | — | h1:3514:577c2a71f4a2797a | 99k3i35yww@main:1573108 |

## 册配置（存包时）

```yaml
id: "2"
volume: 2   # 11-27 用户定册号 1 位，第 2 册一开始就用新册名「2」（方案 Doc 册号位数统一）
cv_version: "0.9.10"   # 11-27 第2册开跑（cv 0.9.10，对本书同 0.9.7）＋底库 b35＋书库 v1
corpus: 2   # 11-28 书库 v2（加第2册补文本 maijing_kanripo_sbck_2.txt；CV0 定，第1册仍钉 1）
title: "脈經 第2冊"
raw_dir: data_full/02
raw_pattern: "{page}.png"
dev_set: [20, 21, 40, 41]
# 不少页无界行，竖线走网格；列距实测 192（12 列框宽约 2300，2026-11-17 全书量）
column_grid: true
col_pitch: 192

# 11-27 第2册 10 页小样（实正文 7 页）：vline_track 开 送审 125、关 94；p24（双行小注密集页）开时 1、2 列整列列线错位成乱码，关后读对。同 01 册关掉。
params:
  border_detect:
    vline_track: false
  # YOLO 整列备选格表按册分文件（整表 sha 进 row_segment 指纹，合一张表会让别册过期）：847 列、带小注 222（11-27 gen，jzcls_v1）
  row_segment:
    alt_cuts: corpus/maijing_yolo_alt_cells_2.jsonl
# 11-28 MJ：Kanripo SBCK 第 2 册范围缺两个半叶（卷三脾胃部「肺氣亭」后＝p18 末–p19 前 8 列；肺大腸部「其脉應」后＝p24 后半–p25 前 4 列）。
# align_ref 只认 references[0]（按页换参校本还没做），故本册改用补文本 corpus/maijing_kanripo_sbck_2.txt（按维基文库补正文，小注仍缺）。
# 判停：p18/19 无对位 138→80（p19 清零）。只影响本册。
references:
  - {file: maijing_kanripo_sbck_2.txt, quality: best, label: kanripo, line_is_column: false, accuracy: mid}   # 合成本（CV0 11-28：标 mid，段的档不能高于它；cv #1979）
  - {file: maijing_wikisource.txt, quality: low, label: wiki, line_is_column: false}
# 职名列（朝散大夫…林億等類次）按列走职名分支，同第 1 册 p11/p37
page_kinds:
  roster_cols:
    5: [2]
    35: [2]
# 维基补文的页（CV0 11-28 要留痕）。cv #1979 起段上可写 accuracy: low；本册钉的 0.9.10 段上只认 pages/kind/ref/note，升 cv 后补 accuracy: low
reference_profile:
  segments:
    - {pages: [18, 19, 24, 25], kind: text, note: "维基补文：Kanripo 缺半叶，p18 末–p19 前 8 列、p24 后半–p25 前 4 列按维基文库补正文，小注无"}
```

## 前后对比

（存包时没给 `--report <diff 目录>`）

## 记事

- 2026-11-28T04:00:39Z ★ 标为 main

## 说明（MJ 11-28）
- 改动：书库 v2（加第 2 册补文本 `corpus/maijing_kanripo_sbck_2.txt`：Kanripo SBCK 缺两个半叶，按维基文库补正文）；2.yaml `references` 首位换补文本、`page_kinds.roster_cols` 5:[2]、35:[2]、reference_profile 段 18/19/24/25 标维基补文。CV0 同意。
- 出 v0.1 判停：算法再处理 262 → 137 格（p19 清零）。剩下看图都不是切分错：缺文处小注（p18 8–11 列、p24 2–5 列、p25 第 1 列）、p10 小注对位次序、p5 职名小字、零星墨点格。
- 待审 676 → 577 / 15,549。中心库 rev 1573108。

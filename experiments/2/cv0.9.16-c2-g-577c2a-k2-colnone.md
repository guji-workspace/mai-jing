# cv0.9.16-c2-g-577c2a-k2-colnone

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
| context_decide | 78 | 0.9.10 | 11-27 19:57 → 11-27 19:57 | 0.1 分 |
| align_ref | 78 | 0.9.16 | 11-27 23:00 → 11-27 23:00 | 0.1 分 |
| char_decide | 78 | 0.9.16 | 11-27 23:00 → 11-27 23:02 | 5.7 分 |
| decide_gate | 78 | 0.9.16 | 11-27 23:02 → 11-27 23:02 | 0.1 分 |

## 基本信息

- 册：2
- 存包：2026-11-28T07:04:04Z
- 基线（存包时该册的 main）：`cv0.9.10-c2-g-577c2a-k2-refpatch`
- 包：`products/99k3i35yww/2/cv0.9.16-c2-g-577c2a-k2-colnone`（1426 个文件，7.7 MB）；取回 `guji products pack fetch 2 --label cv0.9.16-c2-g-577c2a-k2-colnone --to <目录>`

## 版本

| cv | cv commit | 语料库 | 底库 | 字形库钉号 | 人裁指纹 | 中心库 rev（seed_admit 跑时） |
|---|---|---|---|---|---|---|
| 0.9.16 | d8fcaebafe00 | 2 | 35 | — | h1:3514:577c2a71f4a2797a | 99k3i35yww@main:1620333 |

## 册配置（存包时）

```yaml
id: "2"
volume: 2   # 11-27 用户定册号 1 位，第 2 册一开始就用新册名「2」（方案 Doc 册号位数统一）
cv_version: "0.9.16"   # 11-28 升 0.9.16（列级无参照 #2018、char_decide 改名）；11-27 开跑用 0.9.10＋底库 b35
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
  - {file: maijing_kanripo_sbck_2.txt, quality: best, label: kanripo, line_is_column: false, accuracy: mid, form: text, script: faithful}   # 合成本（CV0 11-28：标 mid，段的档不能高于它；cv #1979）
  - {file: maijing_wikisource.txt, quality: low, label: wiki, line_is_column: false, form: text, accuracy: low}
# 职名列（朝散大夫…林億等類次）按列走职名分支，同第 1 册 p11/p37
page_kinds:
  roster_cols:
    5: [2]
    35: [2]
# 维基补文的页（CV0 11-28 要留痕）；缺文处小注两个参校本都没有，按列标无参照（cv #2018，0.9.15 起）
reference_profile:
  segments:
    - {pages: [18, 19, 24, 25], kind: text, accuracy: low, note: "维基补文：Kanripo 缺半叶，p18 末–p19 前 8 列、p24 后半–p25 前 4 列按维基文库补正文，小注无"}
    - {pages: [18], kind: none, cols: ["8-11"], note: "缺文小注"}
    - {pages: [24], kind: none, cols: ["2-5"], note: "缺文小注"}
    - {pages: [25], kind: none, cols: [1], note: "缺文小注（第 4 列下半 Kanripo 有，不标）"}
```

## 前后对比

（存包时没给 `--report <diff 目录>`）

## 记事

- 2026-11-28T07:04:07Z ★ 标为 main

## 说明（MJ 11-28）
- 改动：cv 0.9.10→0.9.16（先 `guji-cv decide migrate-name 2`，align_ref 起重算）；2.yaml 缺文小注按列标无参照（p18 cols 8-11、p24 cols 2-5、p25 col 1，cv #2018），维基补文段 accuracy: low。
- 出 v0.1 判停：算法再处理 137 → 38 格（7 页）：p18 第 1 列小注读乱 10、p10 小注对位 10、p5 职名小字 5、p17 第 1 列小注 5、零星 seg_defect（墨点）。看图都不是切分错。缺文小注改落 lib_unrecognized（32→125）。
- 待审 588 / 15,549。中心库 rev 1620333。标 main 时设 GUJI_AUTO_ONLINE_LISTS=0，未上站。

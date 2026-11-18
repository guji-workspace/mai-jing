# cvdevpg78c29c0bbd65-c--g-e3b0c4-noraise

## 摘要

（存包时没给 `--summary`）

**各步运行**（产物 manifest，最近一轮先后）：

| 步 | 页 | cv | 最后一轮起 → 止（洛杉矶） | 耗时合计 |
|---|---|---|---|---|
| border_detect_gate | 68 | dev+g356920427d5e | 11-17 12:15 → 11-17 12:27 | 0.7 分 |
| page_survey | 68 | dev+g78c29c0bbd65 | 11-17 13:18 → 11-17 17:44 | 0.2 分 |
| invert_detect | 68 | dev+g78c29c0bbd65 | 11-17 13:18 → 11-17 17:45 | 0.5 分 |
| border_detect | 68 | dev+g78c29c0bbd65 | 11-17 13:18 → 11-17 17:45 | 3.7 分 |
| seal_detect | 68 | dev+g78c29c0bbd65 | 11-17 13:18 → 11-17 17:46 | 0.7 分 |
| column_warp | 68 | dev+g78c29c0bbd65 | 11-17 19:45 → 11-17 19:46 | 1.3 分 |
| column_gate | 68 | dev+g78c29c0bbd65 | 11-17 19:46 → 11-17 19:46 | 0.2 分 |
| row_segment | 68 | dev+g78c29c0bbd65 | 11-17 19:46 → 11-17 19:47 | 3.4 分 |
| row_segment_gate | 68 | dev+g78c29c0bbd65 | 11-17 19:47 → 11-17 19:47 | 0.1 分 |
| cell_shrink | 68 | dev+g78c29c0bbd65 | 11-17 19:47 → 11-17 19:48 | 2.5 分 |
| glyph_match | 68 | dev+g78c29c0bbd65 | 11-17 19:48 → 11-17 19:57 | 25.3 分 |
| rare_candidates | 68 | dev+g78c29c0bbd65 | 11-17 19:57 → 11-17 19:57 | 1.8 分 |
| align_ref | 68 | dev+g78c29c0bbd65 | 11-17 19:57 → 11-17 19:57 | 0.0 分 |
| context_decide | 68 | dev+g78c29c0bbd65 | 11-17 19:58 → 11-17 19:58 | 0.0 分 |
| seed_admit | 68 | dev+g78c29c0bbd65 | 11-17 19:58 → 11-17 19:58 | 1.5 分 |

## 基本信息

- 册：01
- 存包：2026-11-18T04:24:40Z；说明：claude：关抬头格(max_raised_hint 0)+借全唐文+glyph_sim_base_v1 全册产物，供第1册切分优化/快审线程取用
- 基线（存包时该册的 main）：—
- 包：`products/99k3i35yww/01/cvdevpg78c29c0bbd65-c--g-e3b0c4-noraise`（1037 个文件，5.1 MB）；取回 `guji products pack fetch 01 --label cvdevpg78c29c0bbd65-c--g-e3b0c4-noraise --to <目录>`

## 版本

| cv | cv commit | 语料库 | 底库 | 字形库钉号 | 人裁指纹 | 中心库 rev（seed_admit 跑时） |
|---|---|---|---|---|---|---|
| dev+g78c29c0bbd65 | 78c29c0bbd65 | — | — | — | h1:0:e3b0c44298fc1c14 | 99k3i35yww@main:1071588 |

## 册配置（存包时）

```yaml
id: "01"
title: "脈經 第1冊"
raw_dir: data_full/01
raw_pattern: "{page}.png"
# 叶10、叶20 各两个半叶（cv 页号：叶 L 的 a/b ＝ 2L−2 / 2L−1；1＝书衣，68＝封底）
dev_set: [18, 19, 38, 39]
# 不少页无界行，竖线走网格；列距实测 192（12 列框宽约 2300，2026-11-17 全书量）
column_grid: true
col_pitch: 192
```

## 前后对比

（存包时没给 `--report <diff 目录>`）

## 记事


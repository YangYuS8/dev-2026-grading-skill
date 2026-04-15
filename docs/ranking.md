# 排行榜与汇总建议

当前主汇总文件是：

- `results/grades.csv`

后续如果要做总分排序，建议再生成：

- `results/leaderboard.csv`
- 或 `results/leaderboard.md`

## 建议统计方式

按 `student_username` 汇总每道题最高成绩，然后再计算总分。

建议字段：

- `student_username`
- `task_01`
- `task_02`
- `task_03`
- `task_04`
- `task_05`
- `total_score`
- `graded_count`

## 缺交处理

如果某题没有提交：

- 该题记 0 分
- 或保留为空，再由统计阶段补 0

这取决于你后面想把排行榜展示成“严格总分榜”还是“完成度榜”。
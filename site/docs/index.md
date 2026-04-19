---
layout: home

hero:
  name: dev-2026 排行榜
  text: 自动根据评分仓库生成的考核结果页面
  tagline: 从 results/leaderboard.csv 构建，适合公开查看当前排名与分数分布
  actions:
    - theme: brand
      text: 查看排行榜
      link: /leaderboard
    - theme: alt
      text: 查看评分仓库
      link: https://github.com/YangYuS8/dev-2026-grading

features:
  - title: 自动更新
    details: 当评分仓库中的 leaderboard.csv 更新后，GitHub Actions 会自动重新构建并部署页面。
  - title: 结构简单
    details: 使用 VitePress 作为静态站点生成器，只展示必要信息，方便维护。
  - title: 适合公开展示
    details: 结果来自仓库中的 CSV 文件，便于后续继续接入更多题目和排行榜统计。
---

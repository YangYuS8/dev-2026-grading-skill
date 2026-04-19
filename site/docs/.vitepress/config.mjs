export default {
  title: 'dev-2026 排行榜',
  description: '根据 results/leaderboard.csv 自动生成的排行榜页面',
  base: '/dev-2026-grading/',
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '排行榜', link: '/leaderboard' }
    ],
    sidebar: [
      {
        text: '导航',
        items: [
          { text: '首页', link: '/' },
          { text: '排行榜', link: '/leaderboard' }
        ]
      }
    ],
    socialLinks: [
      { icon: 'github', link: 'https://github.com/YangYuS8/dev-2026-grading' }
    ],
    footer: {
      message: '由 dev-2026-grading 的结果文件自动生成',
      copyright: 'Copyright © 2026 YangYuS8'
    }
  }
}

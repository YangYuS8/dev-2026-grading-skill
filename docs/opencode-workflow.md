# OpenCode 评分工作流

本仓库专门面向 OpenCode。

## 推荐流程

1. clone 本仓库
2. 进入仓库
3. 启动 `opencode`
4. OpenCode 自动识别仓库中的 skills
5. 执行：

```text
/grade <issue编号>
```

或者：

```text
grade issue <issue编号>
```

6. agent 自动完成：
   - `gh issue view`
   - 解析学生用户名、题目仓库名、提交仓库地址、备注
   - 路由到对应评分 skill
   - clone 学生仓库
   - 评分
   - `gh issue comment`
   - 更新 `results/grades.csv`
   - `node scripts/build_leaderboard.js`
   - 关闭 issue

## 主入口

- `grade-submission`

## 单题评分 skills

- `assessment-html-css-beginner`
- `assessment-js-api-beginner`
- `assessment-python-data-cleaning-beginner`
- `assessment-python-deepseek-cli-beginner`
- `assessment-python-tcp-beginner`

## 辅助脚本

- `scripts/update_grades_csv.js`
- `scripts/build_leaderboard.js`

# OpenCode 评分工作流

本仓库专门面向 OpenCode。

## 关键点

OpenCode 项目内 skills 通常应放在：

```text
.opencode/skills/
```

所以本仓库的评分 skills 已经放到：

```text
.opencode/skills/
```

如果你在仓库根目录直接启动 `opencode`，它更容易按项目内 skill 的方式识别这些技能。

## 推荐流程

1. clone 本仓库
2. 进入仓库根目录
3. 启动 `opencode`
4. OpenCode 读取 `.opencode/skills/`
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

- `.opencode/skills/grade-submission`

## 单题评分 skills

- `.opencode/skills/assessment-html-css-beginner`
- `.opencode/skills/assessment-js-api-beginner`
- `.opencode/skills/assessment-python-data-cleaning-beginner`
- `.opencode/skills/assessment-python-deepseek-cli-beginner`
- `.opencode/skills/assessment-python-tcp-beginner`

## 辅助脚本

- `scripts/update_grades_csv.js`
- `scripts/build_leaderboard.js`

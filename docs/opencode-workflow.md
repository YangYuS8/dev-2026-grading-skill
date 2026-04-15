# OpenCode 评分工作流

本仓库现在专门面向 OpenCode。

## 目标流程

1. clone 本仓库
2. 进入仓库
3. 启动 `opencode`
4. OpenCode 自动识别仓库中的 skills
5. 你执行：

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
   - 关闭 issue

---

## 主入口 skill

主入口 skill：

- `grade-submission`

它负责整套评分流程的路由与收尾。

## 单题评分 skill

- `assessment-html-css-beginner`
- `assessment-js-api-beginner`
- `assessment-python-data-cleaning-beginner`
- `assessment-python-deepseek-cli-beginner`
- `assessment-python-tcp-beginner`

## CSV 更新脚本

- `scripts/update_grades_csv.js`

它负责把评分结果追加写入 `results/grades.csv`。

---

## 建议操作方式

推荐你在 OpenCode 中直接给出这种指令：

```text
grade issue 12 using the grade-submission skill in this repo. after grading, reply to the issue, update results/grades.csv, and close the issue.
```

如果后面你习惯了，再简化成：

```text
/grade 12
```

---

## 当前边界

当前仓库已经具备：

- 评分规则
- issue 提交模板
- 总入口 skill
- CSV 更新脚本

但实际评分文本仍然依赖 OpenCode 去读取具体 skill 后生成。

这正是当前设计的目标，不再考虑 OpenClaw。
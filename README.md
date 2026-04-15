# dev-2026-grading

## 这是什么

这是 `dev-2026` 系列考核题配套的评分规则与评分流程仓库。

它的用途不是给学生做题，而是给 OpenClaw / OpenCode / agent 用来：

- 通过 issue 读取学生提交
- 自动识别题目仓库
- 选择对应评分 skill
- 评分并回帖
- 写入 CSV 汇总
- 关闭 issue

---

## 你想要的使用方式

这套仓库现在是按你要的流程来组织的：

1. clone 仓库
2. 进入仓库
3. 启动 `opencode`
4. `opencode` 自动识别仓库中的 skills
5. 你执行类似：

```text
/grade 12
```

或者：

```text
grade issue 12
```

6. 然后 agent 自动：
   - 用 `gh` 读取 issue
   - 识别题目仓库名
   - 路由到对应评分 skill
   - clone 学生仓库
   - 完成评分
   - 回复 issue
   - 更新 CSV
   - 关闭 issue

---

## 仓库结构

```text
.
├── .github/ISSUE_TEMPLATE/
├── assessment-html-css-beginner/
├── assessment-js-api-beginner/
├── assessment-python-data-cleaning-beginner/
├── assessment-python-deepseek-cli-beginner/
├── assessment-python-tcp-beginner/
├── grade-submission/
├── results/
├── scripts/
└── README.md
```

---

## 主入口 skill

主入口 skill 是：

- `grade-submission`

它就是这套流程的总入口。

它负责：

- 读取 issue
- 解析 issue 内容
- 路由到具体题目的 grading skill
- 回帖
- 调 CSV 更新脚本
- 关闭 issue

也就是说，它不是一个单题评分 skill，而是整个评分流程的 orchestrator。

---

## issue 模板

仓库已经提供学生提交模板：

- `.github/ISSUE_TEMPLATE/submission.yml`

建议你要求学生：

- 不要修改题目仓库名
- 用固定 issue 模板提交

这样你就可以：

- 通过 GitHub 用户名识别学生
- 通过仓库名识别题目

---

## CSV 更新脚本

仓库里现在有一个 **Node 辅助脚本**：

- `scripts/update_grades_csv.js`

用途：

- 将评分结果追加写入 `results/grades.csv`

调用方式：

```bash
node scripts/update_grades_csv.js '{"student_username":"alice","task_repo":"dev-2026-01","submission_repo":"https://github.com/alice/dev-2026-01","score":88,"graded_at":"2026-04-16T00:00:00Z","issue_number":12,"status":"graded","notes":"good work"}'
```

这部分我按你的偏好改成 Node 了，不再把它放在 Python 主流程里。

---

## 对接 OpenCode

推荐流程：

1. `git clone https://github.com/YangYuS8/dev-2026-grading.git`
2. `cd dev-2026-grading`
3. 启动 `opencode`
4. 执行：

```text
/grade <issue编号>
```

或者：

```text
grade issue <issue编号>
```

然后让 agent 使用 `grade-submission` skill 完成后续动作。

---

## 对接 OpenClaw

如果你用 OpenClaw，也可以直接把这里的 skill 目录当作评分规则来源。

推荐逻辑一样：

- 主入口：`grade-submission`
- 单题评分：各自的 `assessment-*`
- CSV 更新：`scripts/update_grades_csv.js`

---

## 当前状态说明

现在这套仓库已经更接近你要的形态了：

- skill-first
- OpenCode / OpenClaw 可读
- issue 流程明确
- Node 负责机械写入 CSV

### 当前已经完成

- 5 道题的独立评分 skill
- 总入口 skill
- issue 模板
- CSV 文件
- Node CSV 更新脚本

### 当前还没彻底自动化到的点

还差最后一小步：

> 让 `grade-submission` 在具体运行环境里，稳定调用 agent 自己去执行单题 skill 并拿回真实评分文本。

也就是说，现在评分规则和流程都已经齐了，剩下的是把它和你实际运行的 OpenCode / OpenClaw 执行方式绑得更深一点。

---

## 当前自检结果

我已经检查过当前结构，当前没有明显结构性问题：

- 5 道题评分 skill 都在
- 总入口 skill 已改成真正的主入口语义
- issue 模板存在
- CSV 存在
- Node 辅助脚本存在

如果你下一步愿意，我就可以继续把：

- `/grade <issue编号>` 的实际执行提示词
- 真实评分结果抽取
- 排行榜生成

这三块再补齐。
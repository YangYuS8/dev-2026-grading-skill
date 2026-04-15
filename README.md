# dev-2026-grading

## 这是什么

这是 `dev-2026` 系列考核题配套的评分规则与自动评分流程仓库。

它的用途不是给学生做题，而是给 agent / 助教 / OpenClaw / OpenCode 用来：

- 按题目自动选择评分 skill
- 读取学生 issue 提交
- 拉取学生仓库
- 完成评分
- 把结果回复到 issue
- 写入 CSV 汇总表
- 关闭 issue

---

## 当前包含的 skill

- `assessment-html-css-beginner`
- `assessment-js-api-beginner`
- `assessment-python-data-cleaning-beginner`
- `assessment-python-deepseek-cli-beginner`
- `assessment-python-tcp-beginner`
- `router-grade-submission`

---

## 一条命令开始接入

```bash
git clone https://github.com/YangYuS8/dev-2026-grading.git
cd dev-2026-grading
```

如果你要给 agent 用，一般接入方式是：

- OpenClaw：把需要的 skill 目录接到 skills 目录，或把整个仓库作为评分规则仓库挂载
- OpenCode：直接让 agent 读取对应 `SKILL.md` 与 `references/` 中的规则文件

---

## issue 提交流程

学生通过 GitHub issue 提交：

- GitHub 用户名
- 题目仓库名
- 自己的提交仓库地址
- 备注

仓库中已经提供 issue 模板：

- `.github/ISSUE_TEMPLATE/submission.yml`

---

## 自动评分脚本

当前仓库已经包含一个**可执行流程骨架脚本**：

- `scripts/grade_issue_submission.py`

它现在可以完成：

1. 读取指定 issue
2. 解析学生用户名、题目仓库名、提交仓库地址
3. 根据仓库名自动选择评分 skill
4. clone 学生仓库
5. 生成标准化评分回复骨架
6. 回帖到 issue
7. 写入 `results/grades.csv`
8. 关闭 issue

### 使用方式

```bash
python scripts/grade_issue_submission.py <issue-number>
```

例如：

```bash
python scripts/grade_issue_submission.py 12
```

---

## 重要说明

当前脚本已经是**真正可执行的 issue 自动处理脚本骨架**，但它现在还没有把“调用具体 grading skill 并生成真实分数”这一步完全自动化。

也就是说，它目前负责的是：

- intake
- 路由
- clone
- 回帖
- 记账
- close

而真正的“细粒度评分”，目前仍然建议由 OpenClaw / OpenCode 读取对应 skill 后完成。

这是一个很务实的拆分：

- 脚本负责流程自动化
- agent 负责评分判断

---

## CSV 汇总

评分结果会写入：

- `results/grades.csv`

当前字段为：

- `student_username`
- `task_repo`
- `submission_repo`
- `score`
- `graded_at`
- `issue_number`
- `status`
- `notes`

### status 说明

- `graded`
- `partial`
- `invalid`
- `error`

这样即使学生有些任务没做完，也可以先留下记录。

---

## 对接 OpenClaw

建议做法：

1. 让 OpenClaw 读取 `router-grade-submission`
2. 由它先完成 issue 路由
3. 再根据仓库名转给对应 skill
4. 最后用统一格式输出结果

---

## 对接 OpenCode

建议做法：

1. clone 本仓库
2. 让 OpenCode 读取对应 `SKILL.md`
3. 按 `rubric.md` 评分
4. 用 `output-format.md` 输出
5. 如有需要，再由脚本统一回写 issue 和 CSV

---

## 当前自检结果

我已经检查过当前仓库，当前没有明显结构性问题：

- 5 道题对应 skill 都存在
- 总入口 skill 已存在
- issue 模板已存在
- CSV 已存在
- 自动脚本骨架已存在

### 当前仍值得继续增强的点

- 让脚本直接调用 agent 并拿到真实评分文本
- 自动更新排行榜 CSV / Markdown
- 防止重复评分的去重逻辑
- 对 issue body 格式异常的更强容错

# dev-2026-grading

## 这是什么

这是 `dev-2026` 系列考核题配套的评分规则仓库。

它的用途不是给学生做题，而是给 agent / 助教 / OpenClaw / OpenCode 用来评分、汇总和回写结果。

目前已经包含这些评分 skill：

- `assessment-html-css-beginner`
- `assessment-js-api-beginner`
- `assessment-python-data-cleaning-beginner`
- `assessment-python-deepseek-cli-beginner`
- `assessment-python-tcp-beginner`
- `router-grade-submission`

---

## 一键安装思路

我按你的要求，把 README 写成更适合“让 agent 直接安装 / 接入”的风格。

如果你使用 OpenClaw / OpenCode，一般思路是：

1. clone 这个仓库
2. 把其中需要的 skill 目录放到你的 skills 目录
3. 或者把整个仓库作为评分规则仓库挂载给 agent

### 对 OpenClaw 的建议用法

把本仓库 clone 到本地后，将需要的 skill 目录链接或复制到 OpenClaw 的 skills 目录中。

例如你自己的评分技能目录可以统一管理为：

```bash
git clone https://github.com/YangYuS8/dev-2026-grading.git
```

然后按你的 OpenClaw skills 管理方式接入。

### 对 OpenCode / Codex 的建议用法

如果是 OpenCode / Codex，一般不一定需要“安装”成系统级 skill，也可以直接：

- clone 这个仓库
- 让 agent 读取对应 skill 的 `SKILL.md`
- 按 rubric 执行评分

也就是说，这个仓库本身既可以当 skill 源，也可以当评分规则仓库。

---

## 适用场景

适用于下面这类工作：

- 批量检查学生提交仓库
- 按固定维度输出分数
- 自动根据仓库名选择题目评分规则
- 配合 issue 提交流程进行自动评分
- 把评分结果回写到 issue
- 把结果汇总到 CSV 文件
- 对学生总分进行排序

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
├── router-grade-submission/
├── results/
└── README.md
```

---

## 总入口 skill 是干什么的

`router-grade-submission` 是总入口 skill。

它的作用是：

1. 通过 `gh` 查看学生提交 issue
2. 读取 issue 中的学生用户名、题目仓库名、提交仓库地址
3. 根据仓库名自动判断该用哪一个评分 skill
4. 拉取学生仓库并评分
5. 把评分结果回复到 issue
6. 把结果写入 `results/grades.csv`
7. 关闭 issue

这样后面你的评分流程就会更接近：

> 学生提 issue -> agent 自动评分 -> 回帖 -> 汇总 -> 关闭 issue

---

## issue 提交流程建议

建议你要求学生：

- 不要修改自己的提交仓库名
- 使用固定 issue 模板提交

这样你就可以：

- 通过 GitHub 用户名识别学生
- 通过仓库名识别题目

例如：

- `dev-2026-01`
- `dev-2026-02`
- `dev-2026-03`
- `dev-2026-04`
- `dev-2026-05`

---

## 结果汇总

评分结果建议写入：

- `results/grades.csv`

建议字段：

- `student_username`
- `task_repo`
- `submission_repo`
- `score`
- `graded_at`
- `issue_number`
- `status`
- `notes`

其中 `status` 可以标记：

- `graded`
- `partial`
- `invalid`
- `error`

这样即使学生有一部分任务留空，也可以记录而不是直接丢掉。

---

## 部分任务留空怎么处理

这个场景我也考虑到了。

建议 agent 评分时遵循：

- **能评分的部分照常评分**
- **缺失的部分明确写进问题项**
- **CSV 里记录 status=partial**
- **不要因为局部缺失就完全不给结果**

也就是说：

- 缺 README，可以扣分但不一定直接作废
- 缺截图，可以记缺失
- 缺核心文件，才考虑低分或 invalid

---

## 当前自检结果

我已经检查过当前评分 skill 的基本结构：

- 每题有独立评分 skill
- rubric 与输出格式分离
- 总入口思路明确
- 可以继续接 `gh` 工作流

当前没有明显结构性错误。

如果后面要真正自动跑完整流程，下一步最值得补的是：

- 一个真正更新 `results/grades.csv` 的脚本
- 一个 issue 自动处理脚本
- 一个总分排行榜生成脚本

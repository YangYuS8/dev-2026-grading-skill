# dev-2026-grading-skill

## 这是什么

这是 `dev-2026` 系列考核题配套的评分 skill 仓库。

它的用途不是给学生做题，而是给 agent / 助教 / OpenClaw / OpenCode 用来评分。

目前已经包含这些评分 skill：

- `assessment-html-css-beginner`
- `assessment-js-api-beginner`
- `assessment-python-data-cleaning-beginner`
- `assessment-python-deepseek-cli-beginner`
- `assessment-python-tcp-beginner`

---

## 适用场景

适用于下面这类工作：

- 批量检查学生提交仓库
- 按固定维度输出分数
- 生成统一格式的优点 / 问题 / 建议
- 配合 OpenClaw 做半自动评分
- 配合 OpenCode / Codex / 其他 coding agent 做人工复核前的初评分

---

## 仓库结构

```text
.
├── assessment-html-css-beginner/
├── assessment-js-api-beginner/
├── assessment-python-data-cleaning-beginner/
├── assessment-python-deepseek-cli-beginner/
├── assessment-python-tcp-beginner/
└── README.md
```

每个 skill 目录通常包含：

- `SKILL.md`
- `references/rubric.md`
- `references/output-format.md`

---

## 如何对接 OpenClaw

如果你使用 OpenClaw，可以把这个仓库作为评分 skill 来源。

典型用法是：

1. 让 agent 先读取学生仓库
2. 再触发对应题目的 grading skill
3. 按 skill 规定的 rubric 打分
4. 输出统一格式结果

一个典型评分流程通常会是：

- 读取题目仓库 README / TASK
- 读取学生提交代码
- 调用对应评分 skill
- 输出总分、分项得分、优点、问题、建议

### 建议评分输出格式

所有 skill 都尽量统一为：

```text
总分：XX / 100

1. xxx：XX / XX
2. xxx：XX / XX
...

优点：
- ...
- ...

问题：
- ...
- ...

建议：
- ...
- ...
```

---

## 如何对接 OpenCode

如果你使用 OpenCode / Codex / 类似 coding agent，也可以把这里的 skill 当成“评分规则仓库”使用。

建议方式：

1. 先把学生仓库 clone 到本地
2. 让 agent 阅读对应 skill 的 `SKILL.md`
3. 再按 `references/rubric.md` 执行评分
4. 用 `references/output-format.md` 输出结果

你可以把它理解成：

- 题目仓库负责告诉学生“做什么”
- grading skill 仓库负责告诉 agent“怎么评”

---

## 当前自检结果

我已经顺手检查了一遍当前 skill 仓库，当前结构没有明显大问题：

- 每道题都有独立 skill
- skill 名称清楚
- rubric 与输出格式分离
- 评分维度和题目目标基本对应
- 输出格式基本统一

目前没有特别明显的结构性错误。

### 当前还可以继续优化的点

如果后面你要大规模批改，可以考虑再补：

- 一个总入口 skill，用来根据仓库名自动选择对应评分 skill
- 对“模板复制痕迹”的更明确判断标准
- 对缺失 README、缺失截图、缺失输出文件的扣分细则
- 对多 agent 并行批改时的统一汇总格式

---

## 建议

如果后面学生人数很多，我建议你把这个仓库继续保持成：

- **题目不放这里**
- **这里只放评分规则**

这样职责会一直很清楚，也方便后续扩展第 6 题、第 7 题。

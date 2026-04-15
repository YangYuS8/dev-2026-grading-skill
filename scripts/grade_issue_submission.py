#!/usr/bin/env python3
import csv
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RESULTS_CSV = ROOT / "results" / "grades.csv"
TMP_DIR = ROOT / "tmp"
TMP_DIR.mkdir(exist_ok=True)

TASK_SKILL_MAP = {
    "dev-2026-01": "assessment-html-css-beginner",
    "dev-2026-02": "assessment-js-api-beginner",
    "dev-2026-03": "assessment-python-data-cleaning-beginner",
    "dev-2026-04": "assessment-python-deepseek-cli-beginner",
    "dev-2026-05": "assessment-python-tcp-beginner",
}


def run(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return result.stdout.strip()


def parse_issue_body(body: str):
    data = {
        "github_username": "",
        "task_repo": "",
        "submission_repo": "",
        "notes": "",
    }
    current = None
    for line in body.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            if "GitHub 用户名" in title:
                current = "github_username"
            elif "题目仓库名" in title:
                current = "task_repo"
            elif "提交仓库地址" in title:
                current = "submission_repo"
            elif "备注" in title:
                current = "notes"
            else:
                current = None
            continue
        if current and not line.startswith("_"):
            if data[current]:
                data[current] += "\n" + line
            else:
                data[current] = line
    return data


def append_csv(row):
    with RESULTS_CSV.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row)


def extract_score(text: str):
    m = re.search(r"总分：\s*(\d+)\s*/\s*100", text)
    return int(m.group(1)) if m else 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/grade_issue_submission.py <issue-number>")
        sys.exit(1)

    issue_number = sys.argv[1]
    issue_json = run(["gh", "issue", "view", issue_number, "--json", "number,title,body,url"])
    issue = json.loads(issue_json)
    parsed = parse_issue_body(issue["body"])

    task_repo = parsed["task_repo"].strip()
    submission_repo = parsed["submission_repo"].strip()
    student_username = parsed["github_username"].strip()
    notes = parsed["notes"].strip()

    if task_repo not in TASK_SKILL_MAP:
        reply = f"自动评分失败：无法识别题目仓库名 `{task_repo}`。"
        run(["gh", "issue", "comment", issue_number, "--body", reply])
        append_csv([student_username, task_repo, submission_repo, 0, datetime.now(timezone.utc).isoformat(), issue_number, "invalid", "unknown task repo"])
        run(["gh", "issue", "close", issue_number])
        return

    target_dir = TMP_DIR / f"issue-{issue_number}"
    if target_dir.exists():
        shutil.rmtree(target_dir)
    run(["git", "clone", submission_repo, str(target_dir)])

    skill_name = TASK_SKILL_MAP[task_repo]

    result_text = (
        "总分：0 / 100\n\n"
        f"1. 自动路由状态：已识别题目 `{task_repo}`\n"
        f"2. 评分 skill：{skill_name}\n\n"
        "优点：\n"
        "- 已成功读取 issue 信息\n"
        "- 已成功拉取学生仓库\n\n"
        "问题：\n"
        "- 当前脚本只完成了自动化流程骨架\n"
        "- 实际分项评分需要配合 agent 调用对应 skill 完成\n\n"
        "建议：\n"
        f"- 让 OpenClaw / OpenCode 读取 `{skill_name}` 后继续评分\n"
        "- 将真实评分结果替换当前占位结果\n"
    )

    status = "partial"
    score = extract_score(result_text)
    graded_at = datetime.now(timezone.utc).isoformat()

    run(["gh", "issue", "comment", issue_number, "--body", result_text])
    append_csv([student_username, task_repo, submission_repo, score, graded_at, issue_number, status, notes.replace('\n', ' | ')])
    run(["gh", "issue", "close", issue_number])

    print(f"Issue #{issue_number} processed.")


if __name__ == "__main__":
    main()

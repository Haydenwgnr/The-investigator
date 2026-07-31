import sys
from datetime import datetime
from pathlib import Path

import ollama

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

EVIDENCE_DIR = Path("evidence")
RUNBOOK_FILE = Path("ir_runbook.md")
REPORTS_DIR = Path("reports")
MODEL = "llama3.2:3b"

SYSTEM_PROMPT = """You are a senior SOC analyst conducting ransomware incident triage.
Analyze the provided evidence logs and incident-response runbook.
Produce a clear, professional Markdown incident report.
For every finding, assign a confidence level (High, Medium, or Low) and briefly explain why.
Flag anything you cannot confirm from the evidence — do not present guesses as facts."""

USER_PROMPT_TEMPLATE = """Using the evidence logs and IR runbook below, write a Markdown incident report with these sections:

1. **Summary** — executive overview of the incident
2. **Timeline** — chronological key events with timestamps; each event must include a confidence tag (High/Medium/Low)
3. **Root Cause** — how the attacker gained access and caused impact; include confidence per claim
4. **MITRE ATT&CK Mapping** — for each finding, list tactic, technique name, technique ID (e.g. T1071.001), and confidence (High/Medium/Low) with a one-line rationale
5. **Runbook Compliance** — which runbook steps appear completed vs. missed (reference step numbers from the runbook)
6. **Recommended Next Actions** — prioritized remediation and investigation steps
7. **Uncertain / Needs Verification** — explicitly list any findings, attributions, or timeline links you are unsure about and what additional evidence would resolve them

Use this confidence scale:
- **High** — directly supported by multiple log entries or clear causal chain
- **Medium** — strongly suggested but inferred from partial or single-source evidence
- **Low** — plausible hypothesis only; insufficient evidence to confirm

--- EVIDENCE LOGS ---
{evidence}

--- IR RUNBOOK ---
{runbook}
"""

# Step 1: Read every log file in the evidence/ folder
evidence_parts = []
for path in sorted(EVIDENCE_DIR.iterdir()):
    if path.is_file():
        evidence_parts.append(f"### {path.name}\n{path.read_text(encoding='utf-8')}")
evidence = "\n\n".join(evidence_parts)

# Step 2: Read the incident-response runbook
runbook = RUNBOOK_FILE.read_text(encoding="utf-8")

# Step 3: Send evidence and runbook to the local Llama model via Ollama
user_prompt = USER_PROMPT_TEMPLATE.format(evidence=evidence, runbook=runbook)
response = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ],
)
report = response["message"]["content"]

# Step 4: Create reports/ if needed and write a timestamped report file
REPORTS_DIR.mkdir(exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
output_path = REPORTS_DIR / f"report_{timestamp}.md"
output_path.write_text(report, encoding="utf-8")

print(f"Report written to {output_path}")

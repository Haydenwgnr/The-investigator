# Investigator Instructions

Capabilities and prompt starters for **The Investigator** SOC Copilot.

**Live app:** [the-investigator-haydenwgnr.streamlit.app](https://the-investigator-haydenwgnr.streamlit.app)

---

## What the app does

1. **Correlate & Triage** — upload one or more log files; the Copilot merges them into a single incident report (threat analysis, MITRE ATT&CK, severity, investigation plan, response plan)
2. **Ask the Investigator** — free-form chat with a senior SOC analyst for follow-up questions
3. **Case Files** — read saved Markdown reports from `reports/`

Powered by Groq (Llama 3.3 70B). API key lives in `.streamlit/secrets.toml` (never commit this file).

---

## Sample prompts

### Phishing / email triage
Explain what a phishing email is to a brand-new help desk employee, then list the 5 red flags they should check first. Be concise and practical.

Can triage suspicious emails — check headers (SPF/DKIM/DMARC, Reply-To), flag urgency/secrecy/authority, recommend out-of-band verification.

### Architecture & policy
How does SAML work in a cloud environment?

What are current encryption standards for VPN in an enterprise network?

What are the pitfalls for AI integration on a network?

### Log analysis (CLI scripts)
Can audit server logs for failed-login and brute-force patterns (see `audit.py`).

Can hunt network beaconing — count `(source → destination:port)` pairs, flag regular-interval C2 (`hunt.py`).

Can merge auth and file logs into one timeline, calculate dwell time login → encryption (`timeline.py`).

### Multi-source correlation
Upload the four logs in `samples/` (firewall, Sysmon, Suricata, Windows) and ask: *What happened on WIN-FIN-07? Map the attack chain and cite evidence from each source.*

Upload `evidence/security_events_2026-06-12.log` and ask: *Summarize the SRV-RDP-01 incident — brute force, persistence, and exfil.*

### Automated pipeline
Runs an automated triage pipeline (GitHub Actions + Ollama `llama3.2:3b`) that reads `evidence/` and `ir_runbook.md`, maps findings to MITRE ATT&CK with confidence scores, and commits a timestamped report to `reports/`.

### Complete loop automation
Runs automated triage loop through app.py on Web API using Docker to automatically write and read from the github repository.

---

## Evidence & samples

| Folder | Contents |
|--------|----------|
| `samples/` | WIN-FIN-07 exercise — `firewall.log`, `sysmon.log`, `suricata.log`, `windows_event.log` |
| `evidence/` | Production-style logs; pushing here triggers the Auto-Triage GitHub Action |
| `reports/` | Generated incident reports (do not edit by hand during CI runs) |
| `ir_runbook.md` | NIST 800-61 phases + verified MITRE technique IDs from attack.mitre.org |

---

## Security reminder

Before every commit, verify no secrets are tracked:

```bash
git ls-files | grep -i secret
```

A key pushed to a public repo is a real incident. Keep API keys in `.streamlit/secrets.toml` only.

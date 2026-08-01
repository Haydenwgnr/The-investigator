# The Investigator

An AI-powered security & network analyst built across 8 weeks.

**Live app:** [the-investigator-haydenwgnr.streamlit.app](https://the-investigator-haydenwgnr.streamlit.app)

## What it does

- **Correlate & Triage** — upload firewall, Sysmon, Windows, Suricata, or other logs; Groq (Llama 3.3 70B) returns one Markdown report with threat analysis, MITRE ATT&CK mapping, severity, and investigation/response plans
- **Ask the Investigator** — chat with a senior SOC analyst persona about the case or general IR questions
- **Case Files** — browse saved triage reports from the `reports/` folder
- **Log tooling** — `audit.py` (brute-force), `hunt.py` (C2 beaconing), `timeline.py` (merged timeline + dwell time)
- **Auto-triage pipeline** — GitHub Actions + Ollama reads `evidence/` and `ir_runbook.md`, writes timestamped reports with confidence scoring

## Skills so far

- **Week 1:** Thinks like a security analyst (prompt library)
- **Week 2:** Can triage suspicious emails — check headers (SPF/DKIM/DMARC, Reply-To), flag urgency/secrecy/authority, recommend out-of-band verification
- **Week 3:** Can audit server logs for failed-login and brute-force patterns (`audit.py`)
- **Week 4:** Can hunt network beaconing (`hunt.py`) and reconstruct an incident timeline from multiple logs (`timeline.py`)
- **Week 5:** Runs an automated triage pipeline (GitHub Actions + Ollama) that reads the IR runbook, maps findings to MITRE ATT&CK, and writes a verified incident report
- **Week 6:** Sample evidence sets (`samples/`) for multi-source correlation exercises (WIN-FIN-07)
- **Week 7:** Streamlit SOC Copilot (`app.py`) — hosted Groq correlation, chat, and case-file browser

## Repo layout

| Path | Purpose |
|------|---------|
| `app.py` | Streamlit SOC Copilot |
| `evidence/` | Log files that trigger auto-triage on push |
| `samples/` | Practice log sets (firewall, Sysmon, Suricata, Windows) |
| `reports/` | Auto-generated and saved incident reports |
| `ir_runbook.md` | NIST 800-61 IR runbook + verified MITRE ATT&CK IDs |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Add your Groq API key to `.streamlit/secrets.toml` (gitignored):

```toml
GROQ_API_KEY = "your-key-here"
```

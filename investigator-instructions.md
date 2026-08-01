Explain what a phishing email is to a brand-new help desk employee,
then list the 5 red flags they should check first. Be concise and
practical.
How does SAML work in a cloud environment
What are current encryption standards for vpn in an enterprise network
What are the pitfalls for ai integration on a network?
Can triage suspicious emails — check headers (SPF/DKIM/DMARC, Reply-To), flag urgency/secrecy/authority, recommend out-of-band verification.
Can audit server logs for failed-login and brute-force patterns (see audit.py).
Can hunt network beaconing (hunt.py) and reconstruct an incident timeline from multiple logs to guide response (timeline.py)
Runs an automated triage pipeline (GitHub Actions + a local Llama 3.2 model via Ollama) that reads the IR runbook, maps findings to MITRE ATT&CK, and writes a verified incident report.
A Streamlit SOC Copilot that correlates four telemetry sources (firewall, Sysmon, Windows, Suricata) via Groq and returns a triaged report with MITRE mapping, severity, and response plan.

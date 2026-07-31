# Ransomware Incident Response Runbook

Concise playbook aligned to **NIST SP 800-61** phases. Use checkboxes to track progress during an active incident.

---

## 1. Preparation

- [ ] 1.1 Maintain offline, encrypted backups tested on a regular schedule
- [ ] 1.2 Document critical assets, owners, and recovery priorities (tier 0/1/2 systems)
- [ ] 1.3 Pre-stage incident contacts: IR lead, legal, PR, cyber insurer, law enforcement liaison
- [ ] 1.4 Keep a current network diagram and asset inventory accessible offline
- [ ] 1.5 Deploy and tune EDR, logging (auth, DNS, firewall, file), and centralized SIEM
- [ ] 1.6 Restrict lateral movement: segment networks, enforce least privilege, disable unused RDP/SSH
- [ ] 1.7 Block or alert on risky egress (unknown IPs, non-standard ports, beaconing patterns)
- [ ] 1.8 Train staff on phishing recognition and out-of-band verification for urgent requests
- [ ] 1.9 Draft and approve this runbook; run tabletop exercises at least annually
- [ ] 1.10 Pre-authorize emergency actions (account disable, VLAN isolation, external IR retainer)

---

## 2. Detection & Analysis

- [ ] 2.1 Confirm the alert: user reports, EDR detection, mass file renames (`.locked`), ransom note
- [ ] 2.2 Open an incident ticket; assign IR lead and start an incident timeline (UTC timestamps)
- [ ] 2.3 Identify scope: affected hosts, shares, user accounts, and business units
- [ ] 2.4 Preserve evidence before changes: snapshot VMs, export logs, image affected endpoints
- [ ] 2.5 Collect auth logs — look for brute force, SUCCESS LOGIN from unusual IPs
- [ ] 2.6 Collect network logs — look for C2 beaconing (regular intervals, fixed payload size)
- [ ] 2.7 Collect file-system logs — first `.locked` rename, ransom note creation (`READ_ME*`)
- [ ] 2.8 Correlate findings: link C2 IP, login source IP, and encryption timeline (dwell time)
- [ ] 2.9 Classify severity and declare incident level; notify leadership per escalation matrix
- [ ] 2.10 Determine ransomware family if possible (note filename, extension, ransom text, IOC hashes)

---

## 3. Containment, Eradication & Recovery

### Containment

- [ ] 3.1 Isolate affected hosts from the network (disable NIC / move to quarantine VLAN)
- [ ] 3.2 Block known malicious IPs/domains at firewall and DNS; do not power off if memory forensics needed
- [ ] 3.3 Disable compromised accounts and reset credentials for privileged users
- [ ] 3.4 Suspend remote access (VPN, RDP, SSH) until scope is understood
- [ ] 3.5 Prevent spread: disable admin shares, restrict SMB, audit scheduled tasks and persistence

### Eradication

- [ ] 3.6 Remove malware, backdoors, and unauthorized tools from all identified hosts
- [ ] 3.7 Rebuild compromised systems from known-good gold images — do not decrypt-in-place as sole fix
- [ ] 3.8 Patch exploited vulnerabilities and close firewall gaps (over-permissive egress, open RDP)
- [ ] 3.9 Rotate all secrets: domain admin, service accounts, API keys, VPN certs
- [ ] 3.10 Verify eradication with AV/EDR full scan and threat-hunt queries for repeat IOCs

### Recovery

- [ ] 3.11 Restore data from offline backups; validate integrity before reconnecting systems
- [ ] 3.12 Bring systems online in priority order; monitor closely for 72+ hours post-restore
- [ ] 3.13 Confirm business-critical services operational; document any data loss window
- [ ] 3.14 **Do not pay ransom unless legal/leadership explicitly approves** — payment does not guarantee recovery

---

## 4. Post-Incident Activity

- [ ] 4.1 Produce a final incident report: timeline, root cause, impact, and actions taken
- [ ] 4.2 Document indicators of compromise (IOCs) and share with ISACs / threat intel feeds
- [ ] 4.3 Conduct a lessons-learned meeting within 5 business days of closure
- [ ] 4.4 Update controls: firewall rules, MFA enforcement, backup strategy, detection rules
- [ ] 4.5 Revise this runbook and training based on gaps found during the incident
- [ ] 4.6 Complete regulatory/contractual notifications (legal determines breach reporting obligations)
- [ ] 4.7 Track remediation tasks to completion with owners and due dates

---

## Quick Reference — Key Metrics to Capture

| Metric | Why it matters |
|--------|----------------|
| Time of first compromise | Sets investigation start boundary |
| Dwell time (login → encryption) | Shows attacker recon/staging window |
| C2 IP + beacon interval | Confirms persistent access before impact |
| First encrypted file timestamp | Defines data-loss and recovery scope |
| Accounts and hosts involved | Drives credential rotation and rebuild list |

---

*Version 1.0 — Ransomware IR Runbook (NIST 800-61)*

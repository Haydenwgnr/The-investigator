Verdict: Spoofed email — external attacker. Confidence: ~95%
This was never sent by Marcus Webb or from Meridian Group's infrastructure. The attacker forged the From header and routed the message through a personal Gmail account originating from Nigeria.

Red flags, ranked by weight:

DKIM hard fail — no valid cryptographic signature from meridiangroup.com. The email was not sent by Meridian's mail servers. This is the single most definitive technical indicator.
Nigerian originating IP (41.223.57.188) — the sending device was in Lagos, not Singapore where "Marcus" claimed to be.
Reply-To mismatch — From shows a Meridian address; Reply-To diverts to mwebb.ceo2026@gmail.com, a purpose-built attacker account. Any "confirmation" Sandra sends goes straight to the fraudster.
SPF softfail — Gmail is not an authorized sender for @meridiangroup.com. The email bypassed Meridian's permitted mail infrastructure entirely.
DMARC p=none — Meridian's policy allows delivery even on authentication failure, which is why the email landed in Sandra's inbox despite failing both DKIM and SPF. This is a configuration gap the attacker likely researched.
Fresh attacker infrastructure — mwebb.ceo2026@gmail.com was registered specifically for this campaign.
Social engineering trifecta — urgency (5 PM deadline), secrecy (tell no one), and authority (CEO impersonation) working in concert to bypass every internal control.
Unreachable sender — conveniently unavailable by phone until Monday, eliminating the one verification step that collapses the fraud instantly.


Verification checklist — what stops this cold:

Call Marcus Webb on a known number (not one from the email)
Do not reply to the email — the Reply-To goes to the attacker
Invoke dual-approval policy; the secrecy instruction is designed to bypass it
Confirm through a separate channel (Slack, Teams, personal text)
Verify Apex Consulting Group through independent sources
Alert IT security and finance regardless of the "tell no one" instruction


Immediate infrastructure fix: Meridian should upgrade DMARC from p=none to p=quarantine or p=reject. That single change would have prevented delivery of this email entirely.

This was Claude AI response, however after going over the details and checklist that the AI came up with, it did find all the vulnerabilities that I saw from a glance. It checked public IP address location and cross referenced
the location the sender claimed to be at, noted social engineering tactics to skip verification in place, DKIM, and reply to mismatch. 

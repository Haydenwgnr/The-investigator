import sys
from datetime import datetime

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

AUTH_LOG = "auth_events.log"
FILE_LOG = "file_events.log"

# Keywords that mark an event as significant
KEY_MARKERS = ("SUCCESS LOGIN", ".locked", "READ_ME")

# Step 1: Read all events from both log files
events = []
for log_file in (AUTH_LOG, FILE_LOG):
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                events.append(line)

# Step 2: Sort events chronologically (each line begins with YYYY-MM-DD HH:MM:SS)
events.sort(key=lambda line: datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S"))

# Step 3: Print the merged timeline, highlighting key events
print("=== Unified Timeline ===")
for event in events:
    is_key = any(marker in event for marker in KEY_MARKERS)
    prefix = "*** KEY EVENT *** " if is_key else ""
    print(f"{prefix}{event}")

# Step 4: Calculate dwell time — minutes from first malicious login to first encrypted file
def parse_time(line):
    return datetime.strptime(line[:19], "%Y-%m-%d %H:%M:%S")

first_login = next(e for e in events if "SUCCESS LOGIN" in e)
first_locked = next(e for e in events if ".locked" in e)
dwell_minutes = (parse_time(first_locked) - parse_time(first_login)).total_seconds() / 60

print()
print(f"Dwell time: {dwell_minutes:.1f} minutes")
print(f"  First malicious login: {first_login[:19]}")
print(f"  First .locked file:    {first_locked[:19]}")

import re
import sys
from collections import Counter

# Ensure UTF-8 output on Windows so the warning symbol prints correctly
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LOG_FILE = "server_access.log"

# Step 1: Open and read the log file
with open(LOG_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Step 2: Keep only lines that mention a failed login
failed_lines = [line for line in lines if "FAILED LOGIN" in line]

# Step 3: Extract the IP address from each failed-login line
ip_pattern = re.compile(r"from (\d+\.\d+\.\d+\.\d+)")
ips = []
for line in failed_lines:
    match = ip_pattern.search(line)
    if match:
        ips.append(match.group(1))

# Step 4: Count how many times each IP appears
ip_counts = Counter(ips)

# Step 5: Print a summary sorted from most to fewest attempts
# Flag IPs with 3+ failures as likely brute-force attacks
BRUTE_FORCE_THRESHOLD = 3

print("=== Failed Login Summary ===")
for ip, count in ip_counts.most_common():
    flag = " ⚠ LIKELY BRUTE FORCE" if count >= BRUTE_FORCE_THRESHOLD else ""
    print(f"{ip}: {count} failed attempt(s){flag}")

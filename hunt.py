import sys
from collections import Counter, defaultdict

# Ensure UTF-8 output on Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

LOG_FILE = "network_traffic.log"

# Step 1: Open and read the network traffic log
with open(LOG_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Step 2: Parse each line and count (source -> destination:port) pairs
pair_counts = Counter()
pair_timestamps = defaultdict(list)

for line in lines:
    line = line.strip()
    if not line:
        continue

    # Each line: time, source IP, '->', destination IP:port, bytes
    parts = line.split()
    timestamp = parts[0]
    source_ip = parts[1]
    destination = parts[3]  # parts[2] is the '->' arrow
    pair = (source_ip, destination)

    pair_counts[pair] += 1
    pair_timestamps[pair].append(timestamp)

# Step 3: Find the pair with the highest connection count
top_pair, top_count = pair_counts.most_common(1)[0]
timestamps = pair_timestamps[top_pair]

# Step 4: Compute average seconds between consecutive connections
def to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 3600 + m * 60 + s

gaps = [to_seconds(timestamps[i + 1]) - to_seconds(timestamps[i])
        for i in range(len(timestamps) - 1)]
avg_gap = sum(gaps) / len(gaps) if gaps else 0

# Step 5: Print the beaconing suspect report
print("=== Beaconing Suspect ===")
print(f"{top_pair[0]} -> {top_pair[1]}")
print(f"Connections: {top_count}")
print(f"Average seconds between connections: {avg_gap:.1f}")
print("Timestamps:")
for ts in timestamps:
    print(f"  {ts}")

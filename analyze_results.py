import json
import os

schemes = ["cubic", "bbr", "copa"]

for scheme in schemes:
    path = f'results/low_latency/{scheme}_datalink_run1.log'
    if os.path.exists(path):
        with open(path) as f:
            stats = json.load(f)
            print(f"{scheme}: RTT={stats['avg_rtt']} ms, Throughput={stats['avg_throughput']} Mbps")
    else:
        print(f"{scheme} stats not found.")


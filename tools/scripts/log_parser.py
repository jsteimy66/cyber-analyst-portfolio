#!/usr/bin/env python3
# Simple log parser to extract IPs and counts from a web access log
import re
from collections import Counter
import sys

ip_re = re.compile(r"(\d+\.\d+\.\d+\.\d+)")
counter = Counter()

with open(sys.argv[1], "r", encoding="utf-8") as f:
    for line in f:
        m = ip_re.search(line)
        if m:
            counter[m.group(1)] += 1

for ip, cnt in counter.most_common(25):
    print(f"{ip}\t{cnt}")

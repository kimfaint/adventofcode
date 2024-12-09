#!/usr/bin/env python3

import sys
from pathlib import Path
import re

filename = sys.argv[0].split(".")[0]
print(filename)

input_file = Path(f"{filename}.txt")
print(input_file)

if not input_file.is_file():
    print(f"ERROR: Input {input_file} is missing!")
    sys.exit(1)

print("Read file into text buffer")
data = open(input_file, 'r').read()
print(data[:1000])

print("Part 1: Find each valid `mul(X,Y)` and multiply, then total")
total = 0
for x, y in re.findall(r"mul\((\d+),(\d+)\)", data):
    total += int(x) * int(y)
print(total)

print("Part 2: Find each valid `mul(X,Y)|do()|dont()` enable/disable and multiply, then total")
total = 0
x = 0
y = 0
enabled = True
for mul, x, y, do, dont in re.findall(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", data):
    if do:
        enabled = True
    elif dont:
        enabled = False
    elif mul and enabled:
        total += int(x) * int(y)
print(total)

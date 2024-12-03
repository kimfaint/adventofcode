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

print("Fine each valid `mul(X,Y)` and multiple, then total")
total = 0
for x, y in re.findall(r"mul\((\d+),(\d+)\)", data):
    total += int(x) * int(y)
print(total)

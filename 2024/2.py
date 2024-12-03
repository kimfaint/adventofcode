#!/usr/bin/env python3

import sys
from pathlib import Path
from pprint import pprint

filename = sys.argv[0].split(".")[0]
print(filename)

input_file = Path(f"{filename}.txt")
print(input_file)

if not input_file.is_file():
    print(f"ERROR: Input {input_file} is missing!")
    sys.exit(1)

print("Get reports")
with open(input_file, 'r') as f:
    reports = [[int(x) for x in line.split()] for line in f.readlines()]
pprint(reports[:10])


def safe(report):
    # Use first two values to work out if increasing or decreasing
    p0 = report[0]
    p1 = report[1]
    if p0 == p1:
        return False, "Neither increasing or decreasing at start"
    elif p1 > p0:
        increasing = True
    else:
        increasing = False
    # Check if all are increasing/decreasing
    # Check adjacent levels shift between 1 and 3
    px = p0
    for x in report[1:]:
        if increasing:
            if x <= px:
                return False, "Not all increasing"
        else:
            if x >= px:
                return False, "Not all decreasing"
        delta = abs(x - px)
        if delta > 3:
            return False, "Level shift > 3"
        px = x
    return True, ""


print("Calculate how many reports are safe")
number_safe = 0
for rep in reports:
    safety, reason = safe(rep)
    rep += [safety, reason]
    if safety:
        number_safe += 1
pprint(reports)

print("Number of safe reports")
print(number_safe)

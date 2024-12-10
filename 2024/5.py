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

print("Read rules and updates")
rules = []
updates = []
blank_line = False
with open(input_file, 'r') as f:
    for line in f.readlines():
        if line == "\n":
            blank_line = True
        elif not blank_line:
            rules.append([int(x) for x in line.strip().split("|")])
        else:
            updates.append([int(x) for x in line.strip().split(",")])
pprint(rules)
pprint(updates)


# Iterate over each update and assess each agains the full list of rules
# adding to correct_updates if by the end no rules are broken
correct_updates = []
for update in updates:
    valid = True
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                valid = False
                break
    if valid:
        correct_updates.append(update)
pprint(correct_updates)

# Add middle numbers in each correct_update
sum = 0
for update in correct_updates:
    sum += update[int(len(update) / 2)]
print(f"{sum = }")

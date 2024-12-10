#!/usr/bin/env python3

import sys
from pathlib import Path
import functools
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
incorrect_updates = []
for update in updates:
    valid = True
    for a, b in rules:
        if a in update and b in update:
            if update.index(a) > update.index(b):
                valid = False
                break
    if valid:
        correct_updates.append(update)
    else:
        incorrect_updates.append(update)

# Add middle numbers in each correct_update
pprint(correct_updates)
correct_sum = 0
for update in correct_updates:
    correct_sum += update[int(len(update) / 2)]


def cmp_rules(l, r):
    """
    If l,r are not in any rules that they are even, return 0
    If l,r are in a rule, if the order is correct, return -1 to indacate order correct, 
    else return 1 to indicate out-of-order
    """
    broken = 0
    for rule in rules:
        if l in rule and r in rule:
            broken = -1
            if l != rule[0]:
                broken = 1
                break
    return broken


# Iterate over incorrect_updates and sort them using the rules
pprint(incorrect_updates)
for update in incorrect_updates:
    update.sort(key=functools.cmp_to_key(cmp_rules))

# Add middle numbers in each correct_update
pprint(incorrect_updates)
incorrect_sum = 0
for update in incorrect_updates:
    incorrect_sum += update[int(len(update) / 2)]

print(f"{correct_sum = }")
print(f"{incorrect_sum = }")

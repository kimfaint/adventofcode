#!/usr/bin/env python3

import sys
from pathlib import Path

filename = sys.argv[0].split(".")[0]
print(filename)

input_file = Path(f"{filename}.txt")
print(input_file)

if not input_file.is_file():
    print(f"ERROR: Input {input_file} is missing!")
    sys.exit(1)

print("Get left_list and right_list")
left_list = []
right_list = []
with open(input_file, 'r') as f:
    for line in f.readlines():
        values = line.split()
        left_list.append(int(values[0]))
        right_list.append(int(values[1]))
print(left_list[:10])
print(right_list[:10])

print("Sort lists")
left_list.sort()
right_list.sort()
print(left_list[:10])
print(right_list[:10])

print("Calculate distances")
distances = []
for i in range(len(left_list)):
    distances.append(abs(left_list[i] - right_list[i]))
print(distances[:10])

print("Calculate similarities (appearances of left list in right list)")
similarities = []
for i in range(len(left_list)):
    similarities.append(left_list[i] * right_list.count(left_list[i]))
print(similarities)

print("Part 1: Sum of distances")
print(sum(distances))

print("Part 2: Sum of similarities")
print(sum(similarities))

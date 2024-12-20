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

print("Read file into 2d array")
data = []
with open(input_file, 'r') as f:
    for line in f.readlines():
        data.append([letter for letter in line.rstrip()])
data_width = len(data[0])
data_height = len(data)


def direction_offset_x_y(direction, x, y):
    """
    Passed direction in degrees, and a set of array x, y coordinates
    return offset x,y array coordinates in that direction
    """
    if direction == 0:
        y -= 1
    elif direction == 45:
        x += 1
        y -= 1
    elif direction == 90:
        x += 1
    elif direction == 135:
        x += 1
        y += 1
    elif direction == 180:
        y += 1
    elif direction == 225:
        x -= 1
        y += 1
    elif direction == 270:
        x -= 1
    elif direction == 315:
        x -= 1
        y -= 1
    return x, y


def look_for_letter(word, i, x, y, direction):
    """
    Look for the i'th letter of word in data at coordinates x, y.
    If found, call recursively with x,y coordinates offset using direction (degrees)
    until final letter found, returning True; or letter not found, returning, False.
    """
    if x < 0 or x >= data_width:
        return False
    if y < 0 or y >= data_height:
        return False
    if data[y][x] != word[i]:
        return False
    if i == len(word) - 1:
        return True
    x, y = direction_offset_x_y(direction, x, y)
    return look_for_letter(word, i + 1, x, y, direction)


def part1():
    matches = 0
    word = "XMAS"
    # Iterate over each letter left to right, top to bottom
    # If find first letter of word, look in all directions for next letter
    for y in range(data_height):
        for x in range(data_width):
            for direction in range(0, 360, 45):
                if data[y][x] == word[0]:
                    if look_for_letter(word, 0, x, y, direction):
                        matches += 1
    print(f"Part 1 {matches = }")


def is_x_mas(x, y):
    """
    Return True is the coorindate x,y is the centre of a 3x3 array
    with "A" in the middle and both diagaonals have "M" on one end and "S" on the other
    """
    if data[y][x] != "A":
        return False
    diagonal1 = data[y - 1][x - 1] + "A" + data[y + 1][x + 1]
    diagonal2 = data[y + 1][x - 1] + "A" + data[y - 1][x + 1]
    masses = ["MAS", "SAM"]
    return diagonal1 in masses and diagonal2 in masses


def part2():
    matches = 0
    # Iterate over each letter left to right, top to bottom
    # but we can start in row/col 1 and finish in -1,
    # because that's as close as we can get to the edge and be able to find a X-MAS.
    # If we find the "A" character, which is allways in the middle,
    # then call x_mas to see if it is the centre on an X_MAS
    for y in range(1, data_height - 1):
        for x in range(1, data_width - 1):
            if is_x_mas(x, y):
                matches += 1
    print(f"Part 2 {matches = }")


part1()
part2()

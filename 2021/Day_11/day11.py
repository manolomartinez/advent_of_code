from sys import argv
from itertools import product, filterfalse
from collections import deque

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star

syntax = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse_line(line):
    return np.array([int(number) for number in list(line[:-1])])


def parse_input(lines):
    return np.array([parse_line(line) for line in lines])


def step(my_array):
    flashed = []
    my_array += 1
    greaterthan9 = my_array > 9
    flashes = greaterthan9.sum()
    if flashes:
        to_flash = [[x, y] for x, y in zip(*np.where(greaterthan9))]
    else:
        return my_array, 0
    while len(to_flash):
        while len(to_flash):
            x, y = to_flash.pop()
            for pos in adjacents(x, y, my_array):
                my_array[pos] += 1
            flashed.append([x, y])
        greaterthan9 = my_array > 9
        to_flash = [
            [x, y] for x, y in zip(*np.where(greaterthan9)) if [x, y] not in flashed
        ]
    my_array[my_array > 9] = 0
    return my_array, len(flashed)


def in_array(x, y, row, cols):
    return 0 <= x <= row - 1 and 0 <= y <= cols - 1


def adjacents(x, y, my_array):
    row, cols = my_array.shape
    adjacents = filterfalse(lambda x: x == (0, 0), product(range(-1, 2), repeat=2))
    raw_positions = [(x + adjx, y + adjy) for adjx, adjy in adjacents]
    positions = [
        position for position in raw_positions if in_array(*position, row, cols)
    ]
    return positions


def calc_result(my_array, steps=100):
    total_flashes = 0
    for _ in range(steps):
        my_array, flashes = step(my_array)
        total_flashes += flashes
    return total_flashes


# 2nd star


def calc_result2(my_array):
    rows, cols = my_array.shape
    cells = rows * cols
    flashes = 0
    counter = 0
    while flashes != cells:
        my_array, flashes = step(my_array)
        counter += 1
    return counter


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    parsed_input = parse_input(data)
    parsed_input2 = parsed_input.copy()
    # First puzzle
    result = calc_result(parsed_input)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = calc_result2(parsed_input2)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

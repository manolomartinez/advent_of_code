from sys import argv
from itertools import product, filterfalse
from collections import deque

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star


def parse_dots(line):
    return np.array([int(number) for number in line.strip().split(",")])


def parse_instructions(line):
    words = line.split()
    inst = words[2]
    k, v = inst.split('=')
    return k, int(v)


def parse_input(lines):
    instructions = []
    dots = []
    current_line = lines.pop()
    while current_line != "\n":
        k, v = parse_instructions(current_line)
        instructions.insert(0, [k, v])
        current_line = lines.pop()
    for line in lines:
        dots.append(parse_dots(line))
    return np.array(dots), instructions


def array_from_dots(dots):
    shape = np.max(dots[:, 0]) + 1, np.max(dots[:, 1]) + 1
    my_array = np.zeros(shape)
    for pair in dots:
        my_array[tuple(pair)] = 1
    return my_array.T


def fold_up(my_array, y):
    before_y = y
    after_y = my_array.shape[0] - y - 1
    offset = before_y - after_y
    if offset > 0:
        padded = np.pad(my_array, ((0, offset), (0, 0)), constant_values = 0) 
    if offset < 0:
        padded = np.pad(my_array, ((-offset, 0), (0, 0)), constant_values = 0) 
        y -= offset
    else:
        padded = my_array
    upper_half = padded[:y, :]
    lower_half_reversed = np.flip(padded[y+1:, :], axis=0)
    return np.logical_or(upper_half, lower_half_reversed).astype(int)


def fold_left(my_array, x):
    before_x = x
    after_x = my_array.shape[1] - x - 1
    offset = before_x - after_x
    if offset > 0:
        padded = np.pad(my_array, ((0, 0), (0, offset)), constant_values = 0) 
    if offset < 0:
        padded = np.pad(my_array, ((0, 0), (-offset, 0)), constant_values = 0) 
        x -= offset
    else:
        padded = my_array
    left_half = padded[:, :x]
    right_half_reversed = np.flip(padded[:, x+1:], axis=1)
    return np.logical_or(left_half, right_half_reversed).astype(int)

def calc_result(my_array, instructions):
    inst = instructions[0]
    if inst[0] == 'x':
        my_array = fold_left(my_array, inst[1])
    else:
        my_array = fold_up(my_array, inst[1])
    return my_array.sum()


# Second star


def calc_result2(my_array, instructions):
    for inst in instructions:
        if inst[0] == 'x':
            my_array = fold_left(my_array, inst[1])
        else:
            my_array = fold_up(my_array, inst[1])
    return my_array


def nice_print(my_array):
    translate = {1: '█', 0:' '}
    for row in my_array:
        print(''.join([translate[num] for num in row]))


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    dots, instructions = parse_input(data)
    # First puzzle
    my_array = array_from_dots(dots)
    result = calc_result(my_array, instructions)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = calc_result2(my_array, instructions)
    print("Second puzzle:")
    nice_print(result)


if __name__ == "__main__":
    main()

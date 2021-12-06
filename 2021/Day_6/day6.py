from sys import argv
from itertools import product

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readline()
    return line


# 1st star


def parse_input(line):
    return [int(number) for number in line[:-1].split(",")]


def init_dict(line):
    school = {}
    for i in range(9):
        school[i] = 0
    for fish in line:
        school[fish] += 1
    return school


def step(school):
    new_school = school.copy()
    for i in range(8, 0, -1):
        new_school[i - 1] = school[i]
    new_school[6] += school[0]
    new_school[8] = school[0]
    return new_school


def evolve(school, days):
    for _ in range(days):
        school = step(school)
    return school


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    parsed_input = parse_input(data)
    school = init_dict(parsed_input)
    # First puzzle
    new_school = evolve(school, 80)
    result = sum(new_school.values())
    print("First puzzle: {}".format(result))
    # Second puzzle
    new_school = evolve(school, 256)
    result = sum(new_school.values())
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

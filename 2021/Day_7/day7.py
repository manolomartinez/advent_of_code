from sys import argv
from itertools import product

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readline()
    return line


# 1st star


def parse_input(line):
    return np.array([int(number) for number in line[:-1].split(",")])


def cost(positions, position):
    return np.abs(positions - np.array([position] * positions.shape[0])).sum()


def all_costs(positions):
    return [
        cost(positions, position)
        for position in range(min(positions), max(positions) + 1)
    ]


def calc_result(positions):
    allcosts = all_costs(positions)
    return min(allcosts)


# 2nd star

costs_per_distance = {}


def cost_per_distance(distance):
    if not distance in costs_per_distance:
        costs_per_distance[distance] = sum(range(1, distance + 1))
    return costs_per_distance[distance]


def cost2(positions, position):
    distances = np.abs(positions - np.array([position] * positions.shape[0]))
    costs = sum(list(map(cost_per_distance, distances)))
    return costs


def all_costs2(positions):
    return [
        cost2(positions, position)
        for position in range(min(positions), max(positions) + 1)
    ]


def calc_result2(positions):
    allcosts = all_costs2(positions)
    return np.min(allcosts)


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    parsed_input = parse_input(data)
    # First puzzle
    result = calc_result(parsed_input)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = calc_result2(parsed_input)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

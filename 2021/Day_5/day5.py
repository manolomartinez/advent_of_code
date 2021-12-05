from sys import argv
from itertools import product

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return lines


# 1st star

def parse_input(lines):
    def parse_line(line):
        init, end = line.split(' -> ')
        return [int(number) for number in init.split(',')], [int(number) for
                number in end.split(',')]
    return [parse_line(line) for line in lines]


def hor_ver(parsed_lines):
    hv = []
    diag = []
    for line in parsed_lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            hv.append(line)
        else:
            diag.append(line)
    return hv, diag


def expand_hv(points):
    init, end = points
    if init[0] > end[0]:
        step_x = -1
    else:
        step_x = 1
    if init[1] > end[1]:
        step_y = -1
    else:
        step_y = 1
    range_x = range(init[0], end[0] + step_x ,step_x)
    range_y = range(init[1], end[1] + step_y ,step_y)
    return list(product(range_x, range_y))


def expand_diag(points):
    translate = {True:1, False:-1}
    init, end = points
    expanded = []
    inc_x = translate[end[0] > init[0]]
    inc_y = translate[end[1] > init[1]]
    for i in range(abs(end[0] - init[0]) + 1):
        expanded.append((init[0] + i * inc_x, init[1] + i * inc_y))
    return expanded


def count(parsed_lines):
    points = {}
    hv, diag = hor_ver(parsed_lines)
    new_points_hv = []
    new_points_diag = []
    for line in hv:
        new_points_hv += expand_hv(line)
    for line in diag:
        new_points_diag += expand_diag(line)
    new_points = new_points_hv + new_points_diag
    for point in new_points:
        if not point in points:
            points[point] = 1
        else:
            points[point] += 1
    return points


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    parsed_lines = parse_input(data)
    hv, diag = hor_ver(parsed_lines)
    # First puzzle
    counts = np.array(list(count(hv).values()))
    result = (counts >= 2).sum()
    print("First puzzle: {}".format(result))
    # Second puzzle
    counts = np.array(list(count(parsed_lines).values()))
    result = (counts >= 2).sum()
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

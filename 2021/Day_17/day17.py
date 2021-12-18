from sys import argv
from itertools import product, zip_longest
from collections import Counter, defaultdict
from functools import reduce
from operator import mul

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readline()
    return line.strip()


# 1st star


def parse_input(line):
    _, _, xstr, ystr = line.split(" ")
    xrange = [int(num) for num in xstr[2:-1].split("..")]
    yrange = [int(num) for num in ystr[2:].split("..")]
    return xrange, yrange


def step(init_pos, dx, dy):
    x, y = init_pos
    x += dx
    y += dy
    if dx != 0:
        dx -= dx / dx
    dy -= 1
    return (x, y), dx, dy


def calc_best(xmin, xmax, ymin, ymax):
    if abs(ymin) > abs(ymax):
        highest_dy = abs(ymin) - 1
        steps = 2 * abs(ymin)
    else:
        return (xmin, ymax)
    for dy in range(highest_dy, 0, -1):
        dx = 1
        while dx <= xmax:
            if check_solution(dx, dy, xmin, xmax, ymin, ymax):
                return (dx, dy)
            dx += 1
    return False


def check_solution(dx, dy, xmin, xmax, ymin, ymax):
    pos = 0, 0
    while pos[1] > ymin or dy > 0:
        prev = pos
        pos, dx, dy = step(pos, dx, dy)
        x, y = pos
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return True
    return False


def calc_result(vels):
    return sum(range(vels[1] + 1))


# 2nd star


def calc_all(xmin, xmax, ymin, ymax):
    solutions = []
    for dy in range(abs(ymin) - 1, ymin - 1, -1):
        for dx in range(xmax + 1):
            if check_solution(dx, dy, xmin, xmax, ymin, ymax):
                solutions.append((dx, dy))
    return solutions


def main():
    input_type = argv[-1] + ".txt"
    line = read_input(input_type)
    xrange, yrange = parse_input(line)
    vels = calc_best(*xrange, *yrange)
    result = calc_result(vels)
    # First puzzle
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = len(calc_all(*xrange, *yrange))
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

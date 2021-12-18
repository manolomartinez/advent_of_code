from sys import argv
from itertools import product, islice
from collections import Counter, defaultdict

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star


def parse_line(line):
    return [int(number) for number in list(line.strip())]


def parse_input(lines):
    return np.array([parse_line(line) for line in lines])


def neighbors(coord, xmax, ymax):
    x, y = coord
    raw_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbors = [
        neighbor
        for neighbor in raw_neighbors
        if 0 <= neighbor[0] < xmax and 0 <= neighbor[1] < ymax
    ]
    return neighbors


def neigh_dict(idx, xmax, ymax):
    dict_ = {}
    for index in idx.reshape(-1, 2):
        dict_[tuple(index)] = neighbors(index, xmax, ymax)
    return dict_


def message_passing(array_):
    my_array = array_.copy()
    init = my_array[0, 0]
    # path = {}
    diagonals = diag_indices(my_array.shape[0])
    for i in range(1, len(diagonals)):
        for j in range(len(diagonals[i])):
            if i < my_array.shape[0]:
                relevant = [j - 1, j]
            else:
                relevant = [j, j + 1]
            minimum = min(
                [
                    (my_array[diagonals[i - 1][rel]], rel)
                    for rel in relevant
                    if 0 <= rel < len(diagonals[i - 1])
                ]
            )
            # path[diagonals[i][j]] = diagonals[i - 1][minimum[1]]
            my_array[diagonals[i][j]] += minimum[0]
    return my_array


def message_passing2(array_):
    my_array = array_.copy()
    init = my_array[0, 0]
    xmax, ymax = my_array.shape
    idx = np.moveaxis(np.indices((xmax, ymax)), 0, -1)
    neighbors = neigh_dict(idx, xmax, ymax)
    old_cums = np.zeros_like(my_array)
    cums = message_passing(my_array)
    counter = 0
    while not np.all(old_cums == cums):
        counter += 1
        indices = idx[cums != old_cums]
        old_cums = cums.copy()
        for index in indices:
            index = tuple(index)
            neighs = neighbors[index]
            for neigh in neighs:
                new_risk = my_array[neigh] + cums[index]
                if new_risk < cums[neigh] or not cums[neigh]:
                    cums[neigh] = new_risk
    return cums[0, 0] - init


def diag_indices(xmax):
    first_half = [
        [(x, y) for x, y in zip(range(xmax - 1, final - 1, -1), range(final, xmax))]
        for final in range(xmax - 1, -1, -1)
    ]
    second_half = [
        [(x, y) for x, y in zip(range(final, -1, -1), range(0, final + 1))]
        for final in range(xmax - 1, -1, -1)
    ]
    return first_half + second_half[1:]


# Second star


def tile_array(my_array):
    dim = my_array.shape[0]
    tiles = np.tile(my_array, (5, 5))
    multipliers = np.vstack([i * np.ones((dim, dim)) for i in range(5)])
    multipliers = np.hstack([i + multipliers for i in range(5)])
    tiles += multipliers.astype(int)
    tiles -= 1
    tiles = tiles % 9
    return tiles + 1


def main():
    input_type = argv[-1] + ".txt"
    lines = read_input(input_type)
    my_array = parse_input(lines)
    my_array2 = my_array.copy()
    # First puzzle
    result = message_passing2(my_array)
    print("First puzzle: {}".format(result))
    # Second puzzle
    tiled = tile_array(my_array2)
    result = message_passing2(tiled)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

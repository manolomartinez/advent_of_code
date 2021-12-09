from sys import argv
from itertools import product

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star


def parse_line(line):
    return [int(number) for number in list(line[:-1])]


def parse_input(lines):
    return np.array([parse_line(line) for line in lines])


def low_points(my_array):
    padded = np.pad(my_array, 1, constant_values=9)
    low_points = []
    coords = []
    xmax, ymax = my_array.shape
    for x, y in product(range(1, xmax + 1), range(1, ymax + 1)):
        if smaller_than_neighbors((x, y), padded):
            low_points.append(padded[x, y])
            coords.append((x - 1, y - 1))
    return np.array(low_points), np.array(coords)


def smaller_than_neighbors(point, my_array):
    x, y = point
    neighbors = (
        my_array[x - 1, y],
        my_array[x + 1, y],
        my_array[x, y - 1],
        my_array[x, y + 1],
    )
    return all([my_array[x, y] < neighbor for neighbor in neighbors])


def calc_result(lows):
    return np.sum(lows + 1)


# 2nd star


def smaller_than_9(point, my_array):
    x, y = point[0], point[1]
    coords = (
        [x - 1, y],
        [x + 1, y],
        [x, y - 1],
        [x, y + 1],
    )
    return [coord for coord in coords if my_array[coord[0], coord[1]] < 9]


def basin(my_array, point):
    padded = np.pad(my_array, 1, constant_values=9)
    basin = []
    to_check = [point]
    while len(to_check):
        for point in to_check:
            neighbors = smaller_than_9([point[0] + 1, point[1] + 1], padded)
            for neighbor in neighbors:
                unpadded = [neighbor[0] - 1, neighbor[1] - 1]
                if not unpadded in basin and not unpadded in to_check:
                    to_check.append(unpadded)
            to_check.remove(point)
            basin.append(point)
    return basin


def calc_result2(my_array, coords):
    basin_sizes = [len(basin(my_array, point)) for point in coords.tolist()]
    return np.array(sorted(basin_sizes)[-3:]).prod()


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    parsed_input = parse_input(data)
    lows, coords = low_points(parsed_input)
    # First puzzle
    result = calc_result(lows)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = calc_result2(parsed_input, coords)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

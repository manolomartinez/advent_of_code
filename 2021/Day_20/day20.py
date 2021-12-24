from sys import argv
from itertools import *
from collections import Counter, defaultdict
from operator import mul
from functools import reduce

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return lines


def to_dec(bits):
    my_array = np.array([int(bit) for bit in bits])
    powers = 2 ** np.arange(my_array.shape[0] - 1, -1, -1)
    return powers @ my_array


pixels = {".": 0, "#": 1}


def parse_input(lines):
    algorithm = [pixels[char] for char in lines[0].strip()]
    image = np.array([[pixels[char] for char in line.strip()] for line in lines[2:]])
    return algorithm, image


# 1st star


def enhance(algo, img_, cv):
    img = img_.copy()
    padded = np.pad(img_, 3, constant_values=cv)
    rows, cols = padded.shape
    new_img = padded.copy()
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            str_arr = padded[i - 1 : i + 2, j - 1 : j + 2]
            position = to_dec(str_arr.reshape(-1))
            new_char = algo[position]
            new_img[i, j] = new_char
    return new_img[1:-1, 1:-1]
    # return new_img


def steps(algo, img_, steps=2):
    img = img_.copy()
    cvs = (0, 1)
    for i in range(steps):
        cv = cvs[i % 2]
        img = enhance(algo, img, cv)
        cv = algo[cv]
    return img


# 2nd star


def main():
    input_type = argv[-1] + ".txt"
    string = read_input(input_type)
    algo, img = parse_input(string)
    result = steps(algo, img).sum()
    # First puzzle
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = steps(algo, img, steps=50).sum()
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

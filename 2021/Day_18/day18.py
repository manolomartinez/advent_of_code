from sys import argv
from itertools import product, zip_longest, permutations
from collections import Counter, defaultdict
from operator import mul
from functools import reduce as r

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return [line.strip() for line in lines]


# 1st star


def encode(line):
    nodes = []
    current = []
    i = 0
    while i < len(line):
        if line[i] == "[":
            current.append(0)
        try:
            number = int(line[i])
            nodes.append(current + [number])
            current = current[:-1] + [1]
        except ValueError:
            pass
        if line[i] == "]":
            current = current[:-2] + [1]
        if line[i] == ",":
            pass
        i += 1
    return nodes


def explode(encoded_):
    encoded = encoded_.copy()
    for i, node in enumerate(encoded):
        if len(node) >= 6 and all([num == 0 or num == 1 for num in node[-6:-2]]):
            if i > 0:
                encoded[i - 1][-1] += node[-1]
            if i + 1 < len(encoded) - 1:
                encoded[i + 2][-1] += encoded[i + 1][-1]
            new_node = node.copy()
            encoded.remove(node)
            encoded.remove(encoded[i])
            encoded.insert(i, new_node[:-2] + [0])
            return encoded
    return encoded


def split(encoded_):
    encoded = encoded_.copy()
    for i, node in enumerate(encoded):
        number = node[-1]
        if node[-1] >= 10:
            pair1 = int(np.floor(number / 2))
            pair2 = int(np.ceil(number / 2))
            new_node1 = node[:-1] + [0, pair1]
            new_node2 = node[:-1] + [1, pair2]
            encoded.remove(node)
            encoded.insert(i, new_node2)
            encoded.insert(i, new_node1)
            return encoded
    return encoded


def add(encoded1, encoded2):
    new_encoded = []
    for node in encoded1:
        new_encoded.append([0] + node)
    for node in encoded2:
        new_encoded.append([1] + node)
    return new_encoded


def reduce(encoded_):
    encoded = encoded_.copy()
    old_encoded = []
    while old_encoded != encoded:
        while old_encoded != encoded:
            old_encoded = encoded
            encoded = explode(encoded.copy())
        old_encoded = encoded
        encoded = split(encoded.copy())
    return encoded


def addred(encoded1, encoded2):
    return reduce(add(encoded1, encoded2))


def calc_magnitude(encoded_):
    mags = encoded_.copy()
    old_mags = []
    while old_mags != mags:
        old_mags = mags
        mags = step_magnitude(mags)
    return mags[0][0]


def step_magnitude(encoded):
    mags = encoded.copy()
    for i, node in enumerate(encoded):
        try:
            if len(node) == len(encoded[i + 1]) and node[:-2] == encoded[i + 1][:-2]:
                mag = node[:-2] + [3 * node[-1] + 2 * encoded[i + 1][-1]]
                mags.remove(encoded[i])
                mags.remove(encoded[i + 1])
                mags.insert(i, mag)
        except IndexError:
            pass
    return sorted(mags)


def homework(encoded):
    added = r(addred, encoded)
    return calc_magnitude(added)


# 2nd star


def homework2(encoded):
    perms = permutations(encoded, 2)
    mags = [calc_magnitude(addred(*perm)) for perm in perms]
    return max(mags)


def main():
    input_type = argv[-1] + ".txt"
    lines = read_input(input_type)
    encoded = [encode(line) for line in lines]
    result = homework(encoded)
    # First puzzle
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = homework2(encoded)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

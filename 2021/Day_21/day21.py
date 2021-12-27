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


def parse_input(lines):
    return [int(line.strip().split(" ")[-1]) for line in lines]


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


# 1st star

deterministic = cycle(range(1, 101))


def play(pos1, pos2, die):
    scores = [0, 0]
    iterable = grouper(cycle(die), 3)
    count = 0
    while True:
        die1 = next(iterable)
        die2 = next(iterable)
        pos1 = (((pos1 + sum(die1)) - 1) % 10) + 1
        count += 3
        scores[0] += pos1
        if scores[0] >= 1000:
            return scores[1] * count
        pos2 = (((pos2 + sum(die2)) - 1) % 10) + 1
        scores[1] += pos2
        count += 3
        if scores[1] >= 1000:
            return scores[0] * count


# 2nd star


dirac = [sum(rolls) for rolls in product(range(1, 4), repeat=3)]


def update_player1(my_dict):
    new_dict = defaultdict(int)
    total1 = 0
    for key1, roll in product(my_dict, dirac):
        (pos1, score1), (pos2, score2) = key1
        new_pos1 = (((pos1 + roll) - 1) % 10) + 1
        new_score1 = score1 + new_pos1
        if new_score1 < 21:
            new_key = ((new_pos1, new_score1), (pos2, score2))
            new_dict[new_key] += my_dict[key1]
        else:
            total1 += my_dict[key1]
    return new_dict, total1


def update_player2(my_dict):
    new_dict = defaultdict(int)
    total2 = 0
    for key1, roll in product(my_dict, dirac):
        (pos1, score1), (pos2, score2) = key1
        new_pos2 = (((pos2 + roll) - 1) % 10) + 1
        new_score2 = score2 + new_pos2
        if new_score2 < 21:
            new_key = ((pos1, score1), (new_pos2, new_score2))
            new_dict[new_key] += my_dict[key1]
        else:
            total2 += my_dict[key1]
    return new_dict, total2


def play2(pos1, pos2):
    init_dict = {((pos1, 0), (pos2, 0)): 1}
    new_dict = init_dict.copy()
    total1 = 0
    total2 = 0
    while new_dict:
        new_dict, new_winners = update_player1(new_dict)
        total1 += new_winners
        new_dict, new_winners = update_player2(new_dict)
        total2 += new_winners
    return total1, total2


def main():
    input_type = argv[-1] + ".txt"
    lines = read_input(input_type)
    pos1, pos2 = parse_input(lines)
    result = play(pos1, pos2, deterministic)
    # First puzzle
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = play2(pos1, pos2)
    print("Second puzzle: {}".format(max(result)))


if __name__ == "__main__":
    main()

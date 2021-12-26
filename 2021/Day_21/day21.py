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


def to_vector(my_dict):
    values_vec = np.array([0] * 3)
    for key in my_dict:
        values_vec[key - 1] = my_dict[key]
    return tuple(values_vec)


def dirac_counts():
    # Groups of three rolls of the Dirac die
    dirac = list(product(range(1, 4), repeat=3))
    # But we only care about how many 1s, 2s and 3s
    counts = [Counter(roll) for roll in dirac]
    dirac_dict = defaultdict(int)
    for count in counts:
        key = to_vector(count)
        dirac_dict[key] += 1
    return dirac_dict


dirac = dirac_counts()
dirac = [sum(rolls) for rolls in product(range(1, 4), repeat=3)]


def update_dict1(my_dict):
    # The keys are (ni, mi, oi) where
    # n: number of 1s, m: number of 2s and o: number of 3s, for the i player.
    # The values are: the number of universes with that combination, the
    # associated position and the associated score
    # This updates the dict for player 1
    new_dict = defaultdict(lambda: (0, (0, 0), (0, 0)))
    for key1, key2 in product(my_dict, dirac):
        player1, player2 = key1
        new_player1 = tuple(np.array(player1) + np.array(key2))
        new_key = (new_player1, player2)
        value1 = (
            np.array(new_dict[new_key][0])
            + np.array(my_dict[key1][0])
            + np.array(dirac[key2])
        )
        pos1, pos2 = my_dict[key1][1]
        new_pos1 = ((pos1 + sum(np.array(key2) * np.array([1, 2, 3])) - 1) % 10) + 1
        score1, score2 = my_dict[key1][2]
        new_score1 = my_dict[key1][2][0] + new_pos1
        if new_score1 >= 21:
            total1 = value1
            del new_dict[new_key]
        else:
            total1 = 0
            new_dict[new_key] = (value1, (new_pos1, pos2), (new_score1, score2))
    return new_dict, total1


def update_dict2(my_dict):
    # The keys are (ni, mi, oi) where
    # n: number of 1s, m: number of 2s and o: number of 3s, for the i player.
    # The values are: the number of universes with that combination, the
    # associated position and the associated score
    # This updates the dict for player 2
    new_dict = defaultdict(lambda: (0, (0, 0), (0, 0)))
    for key1, key2 in product(my_dict, dirac):
        player1, player2 = key1
        new_player2 = tuple(np.array(player2) + np.array(key2))
        new_key = (player1, new_player2)
        value1 = (
            np.array(new_dict[new_key][0])
            + np.array(my_dict[key1][0])
            + np.array(dirac[key2])
        )
        pos1, pos2 = my_dict[key1][1]
        new_pos2 = ((pos2 + sum(np.array(key2) * np.array([1, 2, 3])) - 1) % 10) + 1
        score1, score2 = my_dict[key1][2]
        new_score2 = my_dict[key1][2][1] + new_pos2
        if new_score2 >= 21:
            total2 = value1
            del new_dict[new_key]
        else:
            total2 = 0
            new_dict[new_key] = (value1, (pos1, new_pos2), (score1, new_score2))
    return new_dict, total2


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

from sys import argv
from itertools import permutations

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star


def parse_line(line):
    signals, outputs = line.split(" | ")
    signals = signals.split()
    outputs = outputs[:-1].split()
    return signals, outputs


def parse_input(lines):
    return [parse_line(line) for line in lines]


def uniques_in_line(parsed_line):
    uniques = [2, 3, 4, 7]
    outputs = parsed_line[1]
    count = 0
    for word in outputs:
        if len(word) in uniques:
            count += 1
    return count


def calc_result(parsed_lines):
    counts = [uniques_in_line(line) for line in parsed_lines]
    return sum(counts)


# 2nd star

signals_dict = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

signal_set = [set(list(key)) for key in signals_dict.keys()]


def rewire(signals):
    keys = "abcdefg"
    perms = permutations(keys)
    for perm in perms:
        perm_dict = create_dict(perm)
        translated_signals = [translate_word(word, perm_dict) for word in signals]
        if all([set(list(word)) in signal_set for word in translated_signals]):
            return perm_dict


def translate_word(word, perm_dict):
    return "".join([perm_dict[letter] for letter in word])


def create_dict(perm):
    perm_dict = {}
    values = "abcdefg"
    for k, v in zip(perm, values):
        perm_dict[k] = v
    return perm_dict


def calc_value(parsed_line):
    signals, outputs = parsed_line
    perm_dict = rewire(signals)
    translated_outputs = [translate_word(word, perm_dict) for word in outputs]
    numbers = np.array(
        [signals_dict["".join(sorted(signal))] for signal in translated_outputs]
    )
    return numbers @ (10 ** np.arange(numbers.shape[0] - 1, -1, -1))


def calc_result2(parsed_input):
    values = [calc_value(parsed_line) for parsed_line in parsed_input]
    return sum(values)


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

from sys import argv

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return lines


# 1st star


def parse_input(lines):
    def parse_line(line):
        return np.array([int(number) for number in line[:-1]])

    parsed_lines = np.array([parse_line(line) for line in lines])
    return parsed_lines


def gamma_array(parsed_lines):
    means = parsed_lines.mean(0)
    return (means >= 0.5).astype(int)


def epsilon_array(parsed_lines):
    return (gamma_array(parsed_lines) - 1) % 2


def to_bin(my_array):
    powers = 2 ** np.arange(my_array.shape[0] - 1, -1, -1)
    return (powers * my_array).sum()


def gamma(my_array):
    return to_bin(gamma_array(my_array))


def epsilon(my_array):
    return to_bin(epsilon_array(my_array))


def calc_result(parsed_lines):
    return gamma(parsed_lines) * epsilon(parsed_lines)


# 2nd star


def oxygen(parsed_lines, column=0):
    most_common = gamma_array(parsed_lines)
    filtered = parsed_lines[parsed_lines[:, column] == most_common[column]]
    if filtered.shape[0] == 1:
        return to_bin(np.squeeze(filtered))
    else:
        return oxygen(filtered, column + 1)


def co2(parsed_lines, column=0):
    least_common = epsilon_array(parsed_lines)
    filtered = parsed_lines[parsed_lines[:, column] == least_common[column]]
    if filtered.shape[0] == 1:
        return to_bin(np.squeeze(filtered))
    else:
        return co2(filtered, column + 1)


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    # First puzzle
    parsed = parse_input(data)
    result = calc_result(parsed)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = oxygen(parsed) * co2(parsed)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

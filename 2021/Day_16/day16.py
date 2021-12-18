from sys import argv
from itertools import product, zip_longest
from collections import Counter, defaultdict
from functools import reduce
from operator import mul

import numpy as np

hex_dict = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readline()
    return line.strip()


# 1st star


def to_dec(bits):
    my_array = np.array([int(bit) for bit in bits])
    powers = 2 ** np.arange(my_array.shape[0] - 1, -1, -1)
    return powers @ my_array


def grouper(iterable, n, fillvalue=None):
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def parse_input(line):
    return "".join([hex_dict[sym] for sym in line])


def parse_bits(bits):
    version = to_dec(bits[:3])
    ptype = to_dec(bits[3:6])
    if ptype == 4:
        chars = 0
        literal = ""
        iterable = grouper(bits[6:], 5)
        chunk = "".join(next(iterable))
        chars += 5
        while chunk[0] == "1":
            literal += chunk[1:]
            chunk = "".join(next(iterable))
            chars += 5
        literal += chunk[1:]
        return version, 6 + chars
    else:
        length_id = bits[6]
        if length_id == "0":
            total_length = to_dec(bits[7:22])
            length = 0
            while length < total_length:
                new_version, new_length = parse_bits(bits[22 + length :])
                version += new_version
                length += new_length
            return version, 6 + 1 + 15 + length
        else:
            total_number = to_dec(bits[7:18])
            number = 0
            length = 0
            while number < total_number:
                new_version, new_length = parse_bits(bits[18 + length :])
                version += new_version
                length += new_length
                number += 1
            return version, 6 + 1 + 11 + length


# 2nd star


def parse_bits2(bits):
    version = to_dec(bits[:3])
    ptype = to_dec(bits[3:6])
    if ptype == 4:
        chars = 0
        literal = ""
        iterable = grouper(bits[6:], 5)
        chunk = "".join(next(iterable))
        chars += 5
        while chunk[0] == "1":
            literal += chunk[1:]
            chunk = "".join(next(iterable))
            chars += 5
        literal += chunk[1:]
        return 6 + chars, to_dec(literal)
    else:
        length_id = bits[6]
        values = []
        if length_id == "0":
            total_length = to_dec(bits[7:22])
            length = 0
            while length < total_length:
                new_length, value = parse_bits2(bits[22 + length :])
                length += new_length
                values.append(value)
            value = operators[ptype](values)
            return 6 + 1 + 15 + length, value
        else:
            total_number = to_dec(bits[7:18])
            number = 0
            length = 0
            while number < total_number:
                new_length, value = parse_bits2(bits[18 + length :])
                length += new_length
                values.append(value)
                number += 1
            value = operators[ptype](values)
            return 6 + 1 + 11 + length, value


def sum_packets(values):
    return sum(values)


def prod_packets(values):
    return np.prod(values)


def min_packets(values):
    return min(values)


def max_packets(values):
    return max(values)


def gt_packets(values):
    return 1 if values[0] > values[1] else 0


def lt_packets(values):
    return 1 if values[0] < values[1] else 0


def equal_packets(values):
    return 1 if values[0] == values[1] else 0


operators = {
    0: sum_packets,
    1: prod_packets,
    2: min_packets,
    3: max_packets,
    5: gt_packets,
    6: lt_packets,
    7: equal_packets,
}


def main():
    input_type = argv[-1] + ".txt"
    line = read_input(input_type)
    bits = parse_input(line)
    result, _ = parse_bits(bits)
    # First puzzle
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = parse_bits2(bits)[1]
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

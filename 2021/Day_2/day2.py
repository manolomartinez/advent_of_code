from sys import argv

import numpy as np


def read_input(input_file):
    with open(input_file, 'r') as ifile:
        lines = ifile.readlines()
    return lines

# 1st star

def parse_input(lines):
    def parse_line(line):
        parse_dict = {'forward':[0, 1], 'down':[1, 0], 'up':[-1, 0]}
        return  np.array(parse_dict[line.split()[0]]) * int(line.split()[1])
    parsed_lines = [parse_line(line) for line in lines]
    return parsed_lines


def final_position(parsed_lines):
    init = np.array([0, 0])
    for change in parsed_lines:
        init += change
    return init


def calc_result(pos):
    return pos.prod()


# 2nd star

def parse_input2(lines):
    def parse_line(line):
        command, arg = line.split()
        arg = int(arg)
        return command, arg
    parsed_lines = [parse_line(line) for line in lines]
    return parsed_lines


def final_position2(parsed_lines):
    init = np.array([0, 0])
    aim = 0
    for instruction in parsed_lines:
        command, arg = instruction
        if command == 'forward':
            init += [arg, arg * aim]
        if command == 'up':
            aim -= arg
        if command == 'down':
            aim += arg
    return init


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    # First puzzle
    parsed = parse_input(data)
    pos = final_position(parsed)
    result = calc_result(pos)
    print("First puzzle: {}".format(result))
    # Second puzzle
    parsed = parse_input2(data)
    pos = final_position2(parsed)
    result = calc_result(pos)
    print("Second puzzle: {}".format(result))

if __name__=="__main__":
        main()

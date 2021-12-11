from sys import argv
from itertools import product
from collections import deque

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star

syntax = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse_line(line):
    return list(line)[:-1]


def parse_input(lines):
    return [parse_line(line) for line in lines]


def check_line(line):
    stack = deque("")
    for char in line:
        if char in syntax.keys():
            stack.append(char)
        else:
            try:
                if syntax[stack.pop()] == char:
                    pass
                else:
                    return char
            except IndexError:
                return char


def calc_result(lines):
    my_points = 0
    for line in lines:
        try:
            my_points += points[check_line(line)]
        except:
            pass
    return my_points


# 2nd star

points2 = {")": 1, "]": 2, "}": 3, ">": 4}


def check_line2(line):
    stack = deque("")
    for char in line:
        if char in syntax.keys():
            stack.append(char)
        else:
            try:
                if syntax[stack.pop()] == char:
                    pass
                else:
                    return char
            except IndexError:
                return char
    return stack


def autocomplete(stack):
    completion = []
    while stack:
        unmatched = stack.pop()
        completion.append(syntax[unmatched])
    return completion


def calc_result2(lines):
    stacks = [check_line2(line) for line in lines]
    types = [type(stack) for stack in stacks]
    autocompletions = [autocomplete(stack) for stack in stacks if type(stack) == deque]
    scores = [calc_score(autocompletion) for autocompletion in autocompletions]
    return sorted(scores)[int((len(scores) - 1) / 2)]


def calc_score(autocompletion):
    score = 0
    for symbol in autocompletion:
        score = score * 5 + points2[symbol]
    return score


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

from sys import argv
from itertools import product, filterfalse
from collections import Counter, defaultdict

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star


def parse_template(line):
    return line.strip()


def parse_insertion(line):
    pair, insertion = line.strip().split(" -> ")
    return pair, insertion


def parse_input(lines):
    insertions = {}
    template = parse_template(lines[0])
    for line in lines[2:]:
        k, v = parse_insertion(line)
        insertions[k] = v
    return template, insertions


def step(template, insertions):
    new_template = template
    offset = 0
    for i in range(len(template)):
        try:
            to_insert = insertions[template[i : i + 2]]
            new_template = (
                new_template[: i + 1 + offset]
                + to_insert
                + new_template[i + 1 + offset :]
            )
            offset += 1
        except:
            pass
    return new_template


def run(template, insertions, steps=10):
    for _ in range(steps):
        template = step(template, insertions)
    counts = Counter(template)
    return counts.most_common()[0][1] - counts.most_common()[-1][1]


# Second star


def insertions_to_pairs(insertions):
    pairs = {}
    for k in insertions:
        insert = insertions[k]
        v = ["".join([k[0] + insert]), "".join([insert + k[1]])]
        pairs[k] = v
    return pairs


def template_to_pairs(template):
    template_dict = defaultdict(int)
    for i in range(len(template) - 1):
        template_dict[template[i : i + 2]] += 1
    return template_dict


def new_step(template_dict, pairs):
    new_template_dict = template_dict.copy()
    for pair in template_dict:
        num_pair = template_dict[pair]
        if num_pair > 0:
            new_template_dict[pair] -= template_dict[pair]
            for new_pair in pairs[pair]:
                new_template_dict[new_pair] += num_pair
    return new_template_dict


def new_run(template_dict, pairs, steps=40):
    for _ in range(steps):
        template_dict = new_step(template_dict, pairs)
    return template_dict


def calc_result(template_dict, template):
    frequencies = defaultdict(int)
    for pair in template_dict:
        elem1, elem2 = pair
        frequencies[elem1] += template_dict[pair]
        frequencies[elem2] += template_dict[pair]
    frequencies[template[0]] += 1
    frequencies[template[1]] += 1
    for elem in frequencies:
        frequencies[elem] /= 2
    return int(max(frequencies.values()) - min(frequencies.values()))


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    template, insertions = parse_input(data)
    # First puzzle
    result = run(template, insertions)
    print("First puzzle: {}".format(result))
    # Second puzzle
    pairs = insertions_to_pairs(insertions)
    template_dict = template_to_pairs(template)
    template_dict = new_run(template_dict, pairs)
    result = calc_result(template_dict, template)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

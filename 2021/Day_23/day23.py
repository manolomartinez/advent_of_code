from sys import argv
from collections import defaultdict
from itertools import product

import z3
import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return lines


def flatten(l):
    out = []
    for item in l:
        if isinstance(item, (list, tuple)):
            out.extend(flatten(item))
        else:
            out.append(item)
    return out


test_input = [["B", "A"], ["C", "D"], ["B", "C"], ["D", "A"]]


def beginning_constraint(my_input, positions):
    const = []
    translation = {"A": [0, 1], "B": [2, 3], "C": [4, 5], "D": [6, 7]}
    map_ = [[11, 12], [13, 14], [15, 16], [17, 18]]
    beg = defaultdict(list)
    for col1, col2 in zip(my_input, map_):
        for amphi_type, position in zip(col1, col2):
            beg[amphi_type].append(position)
    for amphi_type in beg:
        for amphi in translation[amphi_type]:
            const.append(
                z3.Or([positions[0][amphi] == position for position in beg[amphi_type]])
            )
    print(const)
    return const


def create_map():
    amphipod_map = defaultdict(dict)
    # moves are: 0:left, 1:right, 2:up, 3:down, 0: stay put
    for i in range(10):
        amphipod_map[i][1] = i + 1
    for i in range(1, 11):
        amphipod_map[i][0] = i - 1
    for i in [12, 14, 16, 18]:
        amphipod_map[i][2] = i - 1
    for i in [11, 13, 15, 17]:
        amphipod_map[i][3] = i + 1
    for i in [11, 13, 15, 17]:
        amphipod_map[i][2] = i - 9
    for i in [2, 4, 6, 8]:
        amphipod_map[i][3] = i + 9
    return amphipod_map


def constraints(my_input, steps=100):
    """
    Amphis are: 0: A1, 1: A2, 2: B1, 3: B2, 4: C1, 5: C2, 6: D1, 7: D2
    """
    amphipod_map = create_map()
    current_amphis = [z3.Int(f"amphi_{step}") for step in range(steps)]
    moves = [z3.Int(f"move_{step}") for step in range(steps)]
    positions = [
        [
            z3.Int(f"{p}_{step}")
            for p in ["A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2"]
        ]
        for step in range(steps)
    ]
    distinct_positions = [z3.Distinct(flatten(positions[step])) for step in
            range(steps)]
    amphi_const = [
        z3.And(0 <= current_amphi, current_amphi < 8)
        for current_amphi in current_amphis
    ]
    beginning_const = beginning_constraint(my_input, positions)
    # all_move_options = [z3.And(0 <= move, move < 4) for move in moves]
    available_moves = [
        [
            [
                [
                    z3.Implies(
                        z3.And(
                            current_amphis[step] == amphi, positions[step][amphi] == i
                        ),
                        z3.Or(
                            [moves[step] == available for available in amphipod_map[i]]
                        ),
                    )
                    for i in range(18)
                ]
            ]
            for amphi in range(8)
        ]
        for step in range(steps - 1)
    ]

    positions_const = [
        [z3.And(0 <= position, position <= 18) for position in positions[step]]
        for step in range(steps)
    ]
    move_in_map = [
        [
            [
                [
                    [
                        z3.Implies(
                            z3.And(
                                current_amphis[step] == amphi,
                                moves[step] == move,
                                positions[step][amphi] == i,
                            ),
                            positions[step + 1][amphi] == amphipod_map[i][move],
                        )
                        for move in amphipod_map[i]
                    ]
                    for i in range(19)
                ]
            ]
            for amphi in range(8)
        ]
        for step in range(steps - 1)
    ]
    stay_put = [
        [
            z3.Implies(
                current_amphis[step] != amphi,
                positions[step][amphi] == positions[step + 1][amphi],
            )
            for amphi in range(8)
        ]
        for step in range(steps - 1)
    ]
    end_constraints = [positions[-1][amphi] == amphi + 11 for amphi in range(8)]

    return (
        distinct_positions,
        amphi_const,
        available_moves,
        positions_const,
        move_in_map,
        stay_put,
        beginning_const,
        end_constraints,
    )


def create_solver(constraints, outfile=None):
    s = z3.Solver()
    for constraint in constraints:
        for const in flatten(constraint):
            s.add(const)
            if outfile:
                with open(outfile, 'a') as ofile:
                    ofile.write(str(const) + '\n')
    return s


def process_model(model):
    final_dict = {}
    final_dict["current_amphis"] = create_sorted_list(model, "amphi")
    final_dict["moves"] = create_sorted_list(model, "move")
    for amphi in ["A1", "A2", "B1", "B2", "C1", "C2", "D1", "D2"]:
        final_dict[amphi] = create_sorted_list(model, amphi)
    return final_dict


def create_sorted_list(model, my_string):
    keys = [key for key in model if my_string in str(key)]
    values = [model[key] for key in keys]
    steps = [int(str(key).split("_")[1]) for key in keys]
    sorted_values = sorted(values, key=steps.index)
    return sorted_values


# 1st star


# 2nd star


def main():
    input_type = argv[-1] + ".txt"
    lines = read_input(input_type)
    # First puzzle
    # print("First puzzle: {}".format(total_on(*things)))
    # Second puzzle
    # print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

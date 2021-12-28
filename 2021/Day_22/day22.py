from sys import argv
from itertools import product, pairwise
from collections import Counter, defaultdict
from operator import mul
from functools import reduce

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return lines


def parse_line(line):
    switch, coords = line.split(" ")
    x, y, z = coords.strip().split(",")
    slices = []
    for coord in [x, y, z]:
        beg, end = coord[2:].split("..")
        slices.append(np.array((int(beg), int(end) + 1)))
    return switch, np.array(slices)


def parse_lines(lines):
    swith_dict = {"on": 1, "off": 0}
    switches = []
    slices = []
    for line in lines:
        switch, slice_ = parse_line(line)
        switches.append(swith_dict[switch])
        slices.append(slice_)
    slices = np.clip(np.stack(slices), -50, +51)
    offset = abs(np.min(slices))
    biggest = abs(np.max(slices))
    slices += offset
    slices = array_to_slices(slices)
    return switches, slices, offset, biggest


def array_to_slices(array):
    slices = []
    for to_slice in array:
        slice_ = (
            slice(to_slice[0, 0], to_slice[0, 1]),
            slice(to_slice[1, 0], to_slice[1, 1]),
            slice(to_slice[2, 0], to_slice[2, 1]),
        )
        slices.append(slice_)
    return slices


# 1st star


def total_on(switches, slices, offset, biggest):
    big_cube = np.zeros(
        (offset + biggest + 1, offset + biggest + 1, offset + biggest + 1)
    )
    for switch, slice_ in zip(switches, slices):
        old_big_cube = big_cube.copy()
        big_cube[slice_] = switch
    return big_cube.sum().astype(int)


# 2nd star


def parse_line2(line):
    switch, coords = line.split(" ")
    x, y, z = coords.strip().split(",")
    slices = []
    for coord in [x, y, z]:
        beg, end = coord[2:].split("..")
        slices.append((int(beg), int(end)))
    return switch, tuple(slices)


def parse_lines2(lines):
    swith_dict = {"on": 1, "off": 0}
    switches = []
    slices = []
    for line in lines:
        switch, slice_ = parse_line2(line)
        switches.append(swith_dict[switch])
        slices.append(slice_)
    return switches, slices


def small_cubes(coords):
    inits = [coord[0] for coord in coords]
    ends = [coord[1] for coord in coords]
    roles = defaultdict(list)
    smols = set()
    for init in inits:
        roles[init] = "i"
    for end in ends:
        if roles[end] == "i":
            roles[end] = "b"
        else:
            roles[end] = "e"
    for point1, point2 in pairwise(sorted(roles)):
        if roles[point1] == "i":
            init = point1
        elif roles[point1] == "e":
            init = point1 + 1
        elif roles[point1] == "b":
            smols.add((point1, point1))
            init = point1 + 1
        if roles[point2] == "i":
            end = point2 - 1
        elif roles[point2] == "e":
            end = point2
        elif roles[point2] == "b":
            smols.add((point2, point2))
            end = point2 - 1
        if init <= end:
            smols.add((init, end))
    return smols


def lilcubes(cuboids):
    xs = [cuboid[0] for cuboid in cuboids]
    ys = [cuboid[1] for cuboid in cuboids]
    zs = [cuboid[2] for cuboid in cuboids]
    xintervals = small_cubes(xs)
    yintervals = small_cubes(ys)
    zintervals = small_cubes(zs)
    total = 0
    relevant_lilcubes = {}
    for i, cuboid in enumerate(cuboids):
        relevant_xs = [
            xinterval
            for xinterval in xintervals
            if cuboid[0][0] <= xinterval[0] <= cuboid[0][1]
            and cuboid[0][0] <= xinterval[1] <= cuboid[0][1]
        ]
        relevant_ys = [
            yinterval
            for yinterval in yintervals
            if cuboid[1][0] <= yinterval[0] <= cuboid[1][1]
            and cuboid[1][0] <= yinterval[1] <= cuboid[1][1]
        ]
        relevant_zs = [
            zinterval
            for zinterval in zintervals
            if cuboid[2][0] <= zinterval[0] <= cuboid[2][1]
            and cuboid[2][0] <= zinterval[1] <= cuboid[2][1]
        ]
        relevant_lilcubes[i] = product(relevant_xs, relevant_ys, relevant_zs)
    return relevant_lilcubes


def combine(switches, cuboids, lilcubes):
    total = 0
    on = set()
    lencuboids = len(cuboids)
    for i, (switch, cuboid) in enumerate(zip(switches, cuboids)):
        print("Calculating reboot step #{0} of {1}".format(i + 1, lencuboids + 1))
        for lilcube in lilcubes[i]:
            if switch:
                if not lilcube in on:
                    total += volume(lilcube)
                    on.add(lilcube)
            elif lilcube in on:
                total -= volume(lilcube)
                on.remove(lilcube)
    return total


def volume(cuboid):
    (x1, x2), (y1, y2), (z1, z2) = cuboid
    return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)


def main():
    input_type = argv[-1] + ".txt"
    lines = read_input(input_type)
    things = parse_lines(lines)
    # First puzzle
    print("First puzzle: {}".format(total_on(*things)))
    # Second puzzle
    switches, cuboids = parse_lines2(lines)
    my_lilcubes = lilcubes(cuboids)
    result = combine(switches, cuboids, my_lilcubes)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

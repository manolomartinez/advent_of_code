from sys import argv
from itertools import *
from collections import Counter, defaultdict
from operator import mul
from functools import reduce

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        string = ifile.read()
    return string


def parse_input(string):
    scanners = string.split("\n\n")
    scanners = [scanner.split("\n")[1:] for scanner in scanners]
    scanners = [
        [[number for number in line.split(",")] for line in scanner]
        for scanner in scanners
    ]
    scanners[-1] = scanners[-1][:-1]
    scanners = [
        np.array([[int(num) for num in row] for row in scanner]) for scanner in scanners
    ]
    return scanners


def calc_rotations():
    start = np.eye(3)
    signs = product([1, -1], repeat=3)
    matrices = permutations(start)
    return np.array(
        [np.array(sign) * matrix for sign, matrix in product(signs, matrices)]
    )


rotations = calc_rotations()


# 1st star


def distances(scanner):
    dists = []
    combs = list(combinations(range(len(scanner)), 2))
    for comb in combs:
        distance = ((scanner[comb[0]] - scanner[comb[1]]) ** 2).sum()
        dists.append(distance)
    return list(zip(dists, combs))


def all_dist_perms(scanners):
    return [distances(scanner) for scanner in scanners]


def common_distances(index1, index2, alldists):
    commons = []
    pairs1 = alldists[index1]
    pairs2 = alldists[index2]
    for pair1, pair2 in product(pairs1, pairs2):
        if pair1[0] == pair2[0]:
            commons.append((pair1[1], pair2[1]))
    return commons


def common_beacons(index1, index2, alldists):
    translation = {}
    dists = common_distances(index1, index2, alldists)
    if dists:
        beacons1 = reduce(lambda x, y: x | y, [set(dist[0]) for dist in dists])
        for beacon in beacons1:
            candidates2 = np.array(
                [list(dist[1]) for dist in dists if beacon in dist[0]]
            )
            most_common, counts = np.unique(candidates2, return_counts=True)
            if max(counts) >= 11:
                translation[beacon] = most_common[counts == max(counts)][0]
    return translation


def find_transform(scanner1, scanner2, translation):
    commons1 = scanner1[tuple([tuple(translation.keys())])]
    commons2 = scanner2[tuple([tuple(translation.values())])]
    all_rots2 = commons2 @ rotations
    distances = commons1 - all_rots2
    for i, distance in enumerate(distances):
        _, idx, counts = np.unique(
            distance, axis=0, return_counts=True, return_index=True
        )
        if max(counts) >= 12:
            j = idx[counts == max(counts)]
            same_distance = (i, j)
            break
    return distances[same_distance], rotations[i]


def all_common_beacons(scanners):
    relevant_transforms = {}
    alldists = all_dist_perms(scanners)
    for (i, scanner1), (j, scanner2) in permutations(enumerate(scanners), 2):
        translation = common_beacons(i, j, alldists)
        if len(translation) >= 12:
            transform = find_transform(scanner1, scanner2, translation)
            relevant_transforms[(i, j)] = transform
    return relevant_transforms


def all_beacons_to_0(scanners_):
    scanners = scanners_.copy()
    total = sum(len(scanner) for scanner in scanners)
    transforms = all_common_beacons(scanners)
    while True:
        for i in range(len(scanners) - 2, -1, -1):
            for j in range(i + 1, len(scanners)):
                try:
                    distance, rotation = transforms[(i, j)]
                    scanners[i] = np.vstack(
                        (scanners[i], (scanners[j] @ rotation + distance).squeeze())
                    )
                    distance, rotation = transforms[(j, i)]
                    scanners[j] = np.vstack(
                        (scanners[j], (scanners[i] @ rotation + distance).squeeze())
                    )
                    scanners[i] = np.unique(scanners[i], axis=0)
                    scanners[j] = np.unique(scanners[j], axis=0)
                    lengths = [len(scanner) for scanner in scanners]
                    if all([lengths[0] == length for length in lengths[1:]]):
                        return transforms, np.unique(scanners[0], axis=0).shape[0]
                except KeyError:
                    pass


# 2nd star


def distances2(scanners, transforms):
    combs = list(combinations(range(len(scanners)), 2))
    distances = transforms.copy()
    distances_old = transforms.copy()
    while not all([comb in distances for comb in combs]):
        for i in distances_old:
            for j in distances_old:
                if i[1] == j[0]:
                    distances[(i[0], j[1])] = (
                        distances_old[i][0] + distances_old[j][0] @ distances_old[i][1],
                        distances_old[j][1] @ distances_old[i][1],
                    )
        distances_old = distances.copy()
    manhattans = [(np.abs(value[0])).sum() for value in distances.values()]
    return max(manhattans)


def main():
    input_type = argv[-1] + ".txt"
    string = read_input(input_type)
    scanners = parse_input(string)
    transforms, result = all_beacons_to_0(scanners)
    # First puzzle
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = distances2(scanners, transforms)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

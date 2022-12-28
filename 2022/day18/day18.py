from itertools import product

import numpy as np

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    return np.loadtxt(myfile, delimiter=",", dtype=int)


def free_faces(cube, cubes):
    # import pdb; pdb.set_trace()
    other_cubes = cubes[~np.all(cubes == cube, axis=1)]
    adjacent = cube + np.array(
        [delta * sign for delta, sign in product(np.eye(3), [1, -1])]
    )
    return sum(np.all(np.any(elem != other_cubes, axis=1)) for elem in adjacent)


def total_area(cubes):
    return sum(free_faces(cube, cubes) for cube in cubes)


def result1(myinput):
    cubes = read_input(myinput)
    return total_area(cubes)


def inside(cube, cubes):
    # import pdb; pdb.set_trace()
    x, y, z = cube
    other_cubes = cubes[~np.all(cubes == cube, axis=1)]
    xplane = other_cubes[np.all(other_cubes[:, (1, 2)] == [y, z], axis=1)][:, 0]
    yplane = other_cubes[np.all(other_cubes[:, (0, 2)] == [x, z], axis=1)][:, 1]
    zplane = other_cubes[np.all(other_cubes[:, (0, 1)] == [x, y], axis=1)][:, 2]
    for axis, plane in zip((x, y, z), (xplane, yplane, zplane)):
        if plane.shape == (0,):
            return False
        elif not (np.any(plane < axis) and np.any(plane > axis)):
            return False
    return True


def find_inside(cubes):
    x_min = min(cubes[:, 0])
    x_max = max(cubes[:, 0])
    y_min = min(cubes[:, 1])
    y_max = max(cubes[:, 1])
    z_min = min(cubes[:, 2])
    z_max = max(cubes[:, 2])
    outside = np.array(
        list(
            product(
                (x_min - 1, x_max + 2), (y_min - 1, y_max + 2), (z_min - 1, z_max + 2)
            )
        )
    )
    mins = tuple(outside[0])
    maxs = tuple(outside[-1])
    outside = set([tuple(elem) for elem in outside])
    old_outside = set()
    while old_outside != outside:
        old_outside = outside.copy()
        outside = set()
        for cube in old_outside:
            adjacent = cube + np.array(
                [delta * sign for delta, sign in product(np.eye(3), [1, -1])], dtype=int
            )
            for adj in adjacent:
                if (
                    np.all(mins <= adj)
                    and np.all(adj <= maxs)
                    and not np.any(np.all(adj == cubes, axis=1))
                ):
                    outside.add(tuple(adj))
    outside = np.array(list(outside))
    all_cubes = np.array(
        list(
            product(
                range(x_min - 1, x_max + 2),
                range(y_min - 1, y_max + 2),
                range(z_min - 1, z_max + 2),
            )
        )
    )
    inside = np.array([])
    for elem in all_cubes:
        if not np.any(np.all(elem == cubes, axis=1)) and not np.any(
            np.all(elem == outside, axis=1)
        ):
            inside = np.append(inside, elem)
    return np.array(list(inside), dtype=int).reshape(-1, 3)


def total_area2(cubes):
    inside = find_inside(cubes)
    total_cubes = np.vstack((cubes, inside))
    return sum(free_faces(cube, total_cubes) for cube in cubes)


def result2(myinput):
    cubes = read_input(myinput)
    return total_area2(cubes)

from itertools import cycle, count, zip_longest

import numpy as np


def import_rocks():
    with open("rocks.txt", "r") as fobj:
        rock_text = fobj.read()
    rocks_text = rock_text.split("\n\n")
    rocks = []
    for rock in rocks_text:
        rocks.append(parse_rock(rock))
    return rocks


def parse_rock(rock):
    parse_dict = {".": 0, "#": 2}
    lines = rock.strip().split("\n")
    return np.array(
        [
            [0, 0]
            + [parse_dict[symbol] for symbol in line]
            + [0 for _ in range(7 - len(line) - 2)]
            for line in lines
        ]
    )


def read_input(myinput):
    with open(myinput, "r") as fobj:
        instructions = fobj.read()
    return list(instructions.strip())


initial_cave = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1],
    ]
)

buffer = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
    ]
)


def down_then_lor(instructions):
    for instruction in instructions:
        yield instruction
        yield "v"


def all_ground_is_covered(cave):
    row = 0
    for col in range(7):
        row = max(row, min(np.where(cave[:, col] == 1)[0]))
    return row + 1


def many_rocks(instructions, max_count=2022, init_cave=initial_cave):
    inst_iter = cycle(down_then_lor(instructions))
    rock_iter = cycle(import_rocks())
    height = 0
    cave = init_cave.copy()
    for count, rock in enumerate(rock_iter):
        cave = fall_rock(rock, cave, inst_iter)
        current_height = cave.shape[0]
        height_needed = all_ground_is_covered(cave)
        cave = cave[: height_needed + 1]
        height += current_height - cave.shape[0]
        if count == max_count - 1:
            break
    return height + cave.shape[0] - init_cave.shape[0], cave


def fall_rock(rock, cave, instructions):
    instructions_dict = {"<": left, ">": right, "v": down}
    cave = np.vstack((rock, buffer, cave))
    while 2 in cave:
        cave = instructions_dict[next(instructions)](cave)
    return cave


def down(cave):
    new_cave = cave.copy()
    ys, xs = np.where(cave == 2)
    if any(cave[y, x] == 1 for y, x in zip(ys + 1, xs)):
        new_cave[new_cave == 2] = 1
        return new_cave
    new_cave[cave == 2] = 0
    for y, x in zip(ys + 1, xs):
        new_cave[y, x] = 2
    first_nonzero_row = np.where(new_cave != 0)[0][0]
    return new_cave[first_nonzero_row:]


def left(cave):
    new_cave = cave.copy()
    ys, xs = np.where(cave == 2)
    if any(xs == 0):
        return new_cave
    if any(cave[y, x] == 1 for y, x in zip(ys, xs - 1)):
        return new_cave
    new_cave[cave == 2] = 0
    for y, x in zip(ys, xs - 1):
        new_cave[y, x] = 2
    return new_cave


def right(cave):
    new_cave = cave.copy()
    ys, xs = np.where(cave == 2)
    if any(xs == 6):
        return new_cave
    if any(cave[y, x] == 1 for y, x in zip(ys, xs + 1)):
        return new_cave
    new_cave[cave == 2] = 0
    for y, x in zip(ys, xs + 1):
        new_cave[y, x] = 2
    return new_cave


def result1(myinput):
    instructions = read_input(myinput)
    height, _ = many_rocks(instructions)
    return height


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, fillvalue='x') --> ABC DEF Gxx
    # grouper('ABCDEFG', 3, incomplete='strict') --> ABC DEF ValueError
    # grouper('ABCDEFG', 3, incomplete='ignore') --> ABC DEF
    args = [iter(iterable)] * n
    if incomplete == "fill":
        return zip_longest(*args, fillvalue=fillvalue)
    if incomplete == "strict":
        return zip(*args, strict=True)
    if incomplete == "ignore":
        return zip(*args)
    else:
        raise ValueError("Expected fill, strict, or ignore")


def equal_to_previous(mylist):
    final = mylist[-5:]
    chunks = grouper(mylist[:-5], 5)
    for i, chunk in enumerate(chunks):
        if final == list(chunk):
            return i, True
    return 0, False


def iterator_from_instructions(instructions):
    return enumerate(cycle(down_then_lor(instructions)))


def find_cycle(instructions, init_cave=initial_cave):
    inst_iter = enumerate(cycle(down_then_lor(instructions)))
    rock_iter = cycle(import_rocks())
    cave = init_cave.copy()
    caves = [cave]
    counters = []
    for rock_counter, rock in zip(count(), rock_iter):
        cave, instruction_counter = fall_rock2(rock, cave.copy(), inst_iter)
        caves.append(cave.copy())
        counters.append([instruction_counter % len(instructions), rock_counter % 5])
        if len(counters) % 5 == 0 and len(counters) >= 10:
            chunk, boolean = equal_to_previous(counters)
            if boolean:
                cycle_start = chunk * 5
                cycle_end = len(counters) - 5
                cave_after_cycle = caves[-1]
                return cycle_start, cycle_end, cave_after_cycle


def fall_rock2(rock, cave, instructions):
    instructions_dict = {"<": left, ">": right, "v": down}
    cave = np.vstack((rock, buffer, cave))
    counter = 0
    while 2 in cave:
        counter, instruction = next(instructions)
        cave = instructions_dict[instruction](cave)
    return cave, counter


def many_rocks2(inst_iter, max_count=2022, init_cave=initial_cave):
    rock_iter = cycle(import_rocks())
    init_height = init_cave.shape[0]
    cave = init_cave.copy()
    for count, rock in enumerate(rock_iter):
        cave, _ = fall_rock2(rock, cave, inst_iter)
        if count == max_count - 1:
            break
    return cave.shape[0] - init_height, cave


def result2(myinput, rocks=1000000000000):
    instructions = read_input(myinput)
    myiter = iterator_from_instructions(instructions)
    start, end, cave_for_rest = find_cycle(instructions)
    height_before, _ = many_rocks2(myiter, max_count=start)
    myiter = iterator_from_instructions(instructions)
    height_after, _ = many_rocks2(myiter, max_count=end)
    cycles = (rocks - start) // (end - start)
    height_all_cycles = cycles * (height_after - height_before)
    rest = (rocks - start) % (end - start)
    if rest != 0:
        height_rest, _ = many_rocks2(myiter, max_count=rest, init_cave=cave_for_rest)
    else:
        height_rest = 0
    return height_before + height_all_cycles + height_rest

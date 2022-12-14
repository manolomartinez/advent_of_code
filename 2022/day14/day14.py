from itertools import product

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return [parse_line(line) for line in lines]


def parse_line(line):
    raw_pairs = line.split(" -> ")
    pairs = [[int(elem) for elem in pair.split(",")] for pair in raw_pairs]
    return pairs


def complete(coord1, coord2):
    return range(min(coord1, coord2), max(coord1, coord2) + 1)


def line_to_coords(line):
    coords = set()
    for i in range(1, len(line)):
        origin = line[i - 1]
        end = line[i]
        for coord in product(complete(origin[0], end[0]), complete(origin[1], end[1])):
            coords.add(coord)
    return coords


def all_coords(lines):
    coords = set()
    for line in lines:
        coords = coords.union(line_to_coords(line))
    return coords


def sand_falls(coords, bottom):
    sand = (500, 0)
    moving = True
    while moving and sand[1] < bottom:
        if (sand[0], sand[1] + 1) not in coords:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in coords:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in coords:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            moving = False
            coords.add(sand)
    return coords


def pour_sand(coords, bottom):
    old_coords = set()
    new_coords = coords.copy()
    while len(new_coords) > len(old_coords):
        old_coords = new_coords.copy()
        new_coords = sand_falls(new_coords.copy(), bottom)
    return new_coords


def result1(myinput):
    coords = all_coords(read_input(myinput))
    new_coords = pour_sand(coords.copy(), max(coord[1] for coord in coords))
    return len(new_coords) - len(coords)


def sand_falls2(coords, bottom):
    sand = (500, 0)
    moving = True
    while moving and sand[1] < bottom:
        if (sand[0], sand[1] + 1) not in coords:
            sand = (sand[0], sand[1] + 1)
        elif (sand[0] - 1, sand[1] + 1) not in coords:
            sand = (sand[0] - 1, sand[1] + 1)
        elif (sand[0] + 1, sand[1] + 1) not in coords:
            sand = (sand[0] + 1, sand[1] + 1)
        else:
            moving = False
    coords.add(sand)
    return coords


def pour_sand2(coords, bottom):
    new_coords = coords.copy()
    while (500, 0) not in new_coords:
        new_coords = sand_falls2(new_coords.copy(), bottom)
    return new_coords


def result2(myinput):
    coords = all_coords(read_input(myinput))
    bottom = max(coord[1] for coord in coords) + 2
    new_coords = pour_sand2(coords.copy(), bottom)
    not_rock = [coord for coord in new_coords if coord[1] < bottom]
    return len(not_rock) - len(coords)

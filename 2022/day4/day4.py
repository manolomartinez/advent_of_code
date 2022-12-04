from math import copysign

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return lines


def parse_line(line):
    pair1, pair2 = line.strip("\n").split(",")
    return [[int(number) for number in pair.split("-")] for pair in (pair1, pair2)]


def full_overlap(pairs):
    pair1, pair2 = pairs
    start_offset = pair1[0] - pair2[0]
    end_offset = pair1[1] - pair2[1]
    if not start_offset or not end_offset:
        return True
    overlap = copysign(1, start_offset) * copysign(1, end_offset)
    return overlap < 0


def result1(myfile):
    pairs = [parse_line(line) for line in read_input(myfile)]
    return sum(full_overlap(two_pairs) for two_pairs in pairs)


def partial_overlap(pairs):
    pair1, pair2 = pairs
    return not (pair1[0] > pair2[1] or pair2[0] > pair1[1])


def result2(myfile):
    pairs = [parse_line(line) for line in read_input(myfile)]
    return sum(partial_overlap(two_pairs) for two_pairs in pairs)

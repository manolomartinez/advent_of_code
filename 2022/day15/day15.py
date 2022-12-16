from re import compile
from itertools import product

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return [parse_line(line) for line in lines]


def parse_line(line):
    p = compile(r"Sensor at x=|, y=|: closest beacon is at x=|, y=|\n")
    return [int(number) for number in p.split(line)[1:-1]]


def distance(x, y, z, t):
    return abs(x - z) + abs(y - t)


def no_beacon(x, y, z, t):
    # this is too ineffcient
    points = set()
    manhattan = distance(x, y, z, t)
    signs = product([1, -1], repeat=2)
    distances = zip(range(0, manhattan + 1), range(manhattan, -1, -1))
    for dist, sign in product(distances, signs):
        point = (x + dist[0] * sign[0], y + dist[1] * sign[1])
        points.add(point)
    return points


def no_beacons_in_line(parsed, line):
    intervals = []
    for sensor_beacon in parsed:
        dist = distance(*sensor_beacon)
        dist_y = abs(sensor_beacon[1] - line)
        if dist_y <= dist:
            dist_x = abs(dist - dist_y)
            intervals.append([sensor_beacon[0] - dist_x, sensor_beacon[0] + dist_x])
    return sorted(intervals)


def consolidate(interval1, interval2):
    intervals12 = interval1 + interval2
    intervals21 = interval2 + interval1
    sorted_interval = sorted(intervals12)
    # overlap
    if (
        sorted_interval not in (intervals12, intervals21)
        or sorted_interval[1] == sorted_interval[2]
    ):
        return [[min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]]
    # one starts before the other ends
    return [interval1, interval2]


def consolidate_all(intervals):
    consolidated = [intervals[0]]
    for interval in intervals[1:]:
        consolidated = consolidated[0:-1] + consolidate(consolidated[-1], interval)
    return consolidated


def result1(myinput):
    parsed = read_input(myinput)
    intervals = no_beacons_in_line(parsed, 2000000)
    consolidated = consolidate_all(intervals)
    return sum(abs(interval[0] - interval[1]) for interval in consolidated)


def result2(myinput):
    parsed = read_input(myinput)
    consolidated = []
    for line in range(4000001):
        intervals = no_beacons_in_line(parsed, line)
        consolidated.append(consolidate_all(intervals))
    for y, consol in enumerate(consolidated):
        if len(consol) > 1:
            return 4000000 * (consol[0][1] + 1) + y

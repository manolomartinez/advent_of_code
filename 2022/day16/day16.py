from itertools import product, filterfalse
from collections import OrderedDict, defaultdict
from bisect import insort
from copy import deepcopy

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return [parse_line(line) for line in lines]


def parse_line(line):
    words = line.split()
    rate = (words[1], int(words[4][5:-1]))
    tunnels = [word.strip(",") for word in words[9:]]
    return rate, (rate[0], tunnels)


def create_cave(lines):
    cave = [dict(), dict()]
    for rate, tunnels in lines:
        cave[0][rate[0]] = rate[1]
        cave[1][tunnels[0]] = {(tunnel, 1) for tunnel in tunnels[1]}
    return cave


def optimize_cave(cave):
    rates, original_tunnels = cave
    optimized_tunnels = defaultdict(set)
    done = False
    while not done:
        for tunnel in original_tunnels:
            for next_tunnel in original_tunnels[tunnel]:
                actual_next, minutes = next_tunnel
                if rates[actual_next] == 0 and actual_next != "AA":
                    for following_tunnel in original_tunnels[actual_next]:
                        if following_tunnel[0] != tunnel:
                            optimized_tunnels[tunnel].add(
                                (following_tunnel[0], minutes + 1)
                            )
                else:
                    optimized_tunnels[tunnel].add((next_tunnel[0], minutes))
        done = optimized_tunnels == original_tunnels
        original_tunnels = optimized_tunnels.copy()
        optimized_tunnels = defaultdict(set)
    final_tunnels = dict(
        (tunnel, tunnels)
        for tunnel, tunnels in original_tunnels.items()
        if rates[tunnel] != 0 or tunnel == "AA"
    )
    return rates, final_tunnels


def release(rates, opened):
    total = 0
    for tunnel in rates:
        if opened[tunnel]:
            total += rates[tunnel]
    return total


def all_paths(cave):
    """
    Calculate time from every tunnel to every other tunnel
    """
    _, original_routes = cave
    optimized_routes = deepcopy(original_routes)
    original_routes = {}
    while original_routes != optimized_routes:
        original_routes = deepcopy(optimized_routes)
        for tunnel in original_routes:
            for following1 in original_routes[tunnel]:
                for following2 in original_routes[following1[0]]:
                    if (
                        not any(
                            following2[0] == following[0]
                            for following in original_routes[tunnel]
                        )
                        and following2[0] != tunnel
                    ):
                        optimized_routes[tunnel].add(
                            (following2[0], following1[1] + following2[1])
                        )
                    else:
                        for following in original_routes[tunnel]:
                            if (
                                following[0] == following2[0]
                                and following[1] > following1[1] + following2[1]
                            ):
                                try:
                                    optimized_routes[tunnel].remove(following)
                                    optimized_routes[tunnel].add(
                                        (following[0], following1[1] + following2[1])
                                    )
                                except KeyError:
                                    pass
    return optimized_routes

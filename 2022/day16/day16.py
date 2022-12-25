from itertools import pairwise, product
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
        cave[1][tunnels[0]] = {tunnel: 1 for tunnel in tunnels[1]}
    return cave


def optimize_cave(cave):
    rates, original_tunnels = cave
    optimized_tunnels = deepcopy(original_tunnels)
    done = False
    while not done:
        for tunnel in original_tunnels:
            for next_tunnel in original_tunnels[tunnel]:
                if rates[next_tunnel] == 0 and next_tunnel != "AA":
                    for following_tunnel in original_tunnels[next_tunnel]:
                        if (
                            following_tunnel != tunnel
                            and not following_tunnel in optimized_tunnels[tunnel]
                        ):
                            optimized_tunnels[tunnel][following_tunnel] = (
                                original_tunnels[tunnel][next_tunnel]
                                + original_tunnels[next_tunnel][following_tunnel]
                            )
                    # del optimized_tunnels[tunnel][next_tunnel]
                # else:
                #    optimized_tunnels[tunnel].add((next_tunnel[0], minutes))
        done = optimized_tunnels == original_tunnels
        original_tunnels = deepcopy(optimized_tunnels)
    prefinal_tunnels = dict(
        (tunnel, tunnels)
        for tunnel, tunnels in original_tunnels.items()
        if rates[tunnel] != 0 or tunnel == "AA"
    )
    final_tunnels = deepcopy(prefinal_tunnels)
    for tunnel in prefinal_tunnels:
        for next_tunnel in prefinal_tunnels[tunnel]:
            if rates[next_tunnel] == 0 and next_tunnel != "AA":
                del final_tunnels[tunnel][next_tunnel]
    return rates, final_tunnels


def release(rates, opened):
    total = 0
    for tunnel in rates:
        if opened[tunnel]:
            total += rates[tunnel]
    return total


def all_paths(cave):
    """
    Calculate budget from every tunnel to every other tunnel
    """
    _, original_routes = cave
    optimized_routes = deepcopy(original_routes)
    original_routes = {}
    while original_routes != optimized_routes:
        original_routes = deepcopy(optimized_routes)
        for tunnel in original_routes:
            for following1 in original_routes[tunnel]:
                for following2 in original_routes[following1]:
                    if not following2 in original_routes[tunnel]:
                        optimized_routes[tunnel][following2] = (
                            original_routes[tunnel][following1]
                            + original_routes[following1][following2]
                        )
                    else:
                        for following in original_routes[tunnel]:
                            if (
                                following == following2
                                and original_routes[tunnel][following]
                                > original_routes[tunnel][following1]
                                + original_routes[following1][following2]
                            ):
                                try:
                                    optimized_routes[tunnel][following] = (
                                        original_routes[tunnel][following1]
                                        + original_routes[following1][following2]
                                    )
                                except KeyError:
                                    pass
    return optimized_routes


path_values = {}


def path_value(distances, rates, path):
    if tuple(path) in path_values:
        return path_values[tuple(path)]
    else:
        value = 0
        time = 0
        for first, second in pairwise(path):
            time += distances[second][first] + 1
            if time > 30:
                return 0
            else:
                value += rates[second] * (30 - time)
        path_values[tuple(path)] = value
        return value


def insert_or_append(mylist, value, index):
    if index != "a":
        mylist.insert(index, value)
    else:
        mylist.append(value)


def greedy_add(distances, rates, path=["AA"]):
    available = list(distances.keys())
    for tunnel in path:
        available.remove(tunnel)
    path_sequence = [path]
    available_sequence = [available]
    # import pdb

    # pdb.set_trace()
    overall_max_value = 0
    while len(available) > 0:
        current_path = []
        max_value = 0
        value_candidates = []
        path_candidates = []
        print(f"path before: {path}")
        for tunnel, index in product(available, list(range(1, len(path))) + ["a"]):
            path_candidate = path.copy()
            insert_or_append(path_candidate, tunnel, index)
            path_candidates.append(path_candidate.copy())
            # print(f"path_candidate: {path_candidate}")
            value_candidates.append(path_value(distances, rates, path_candidate))
            # print(f"value_candidate: {value_candidate}")
        max_value = max(value_candidates)
        if max_value == 0:
            path_values[tuple(path)] = 0
        else:
            current_path = path_candidates[value_candidates.index(max_value)]
            #print(f"current_path: {current_path}")
            print(max_value)
            path = current_path.copy()
            if max_value > overall_max_value:
                overall_max_value = max_value
        print(f"path after: {path}")
        available = [tunnel for tunnel in available if not tunnel in path]
    return path, overall_max_value

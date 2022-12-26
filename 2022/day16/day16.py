from copy import deepcopy
from itertools import permutations

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


def available(current, total):
    return (elem for elem in total if not elem in current)


def brute_force(distances, rates):
    all_tunnels = list(distances.keys())
    max_value = 0
    # import pdb; pdb.set_trace()
    branches = [[["AA"], 0, 0]]
    while len(branches) > 0:
        path, time, value = branches.pop()
        for tunnel in available(path, all_tunnels):
            new_path = path.copy()
            new_path.append(tunnel)
            new_time = time + distances[path[-1]][tunnel] + 1
            new_value = value + rates[tunnel] * (30 - new_time)
            if new_time <= 30:
                if new_value > max_value:
                    max_value = new_value
                    # print(max_value)
                    # print(new_path)
            if new_time < 30 and set(new_path) != set(all_tunnels):
                branches.append([new_path, new_time, new_value])
                # print(new_path, new_time, new_value)
    return max_value


def result1(myinput):
    lines = read_input(myinput)
    pre_cave = create_cave(lines)
    cave = optimize_cave(pre_cave)
    distances = all_paths(cave)
    rates, _ = cave
    value = brute_force(distances, rates)
    return value


def brute_force2(distances, rates):
    all_tunnels = list(distances.keys())
    max_value = 0
    branches = [[["AA"], ["AA"], 0, 0, 0, 0]]
    while len(branches) > 0:
        path_h, path_e, time_h, value_h, time_e, value_e = branches.pop()
        for tunnel_h, tunnel_e in permutations(
            available(path_h + path_e, all_tunnels), r=2
        ):
            # Santa moves
            new_path_h = path_h.copy()
            new_path_h.append(tunnel_h)
            new_time_h = time_h
            new_time_h += distances[path_h[-1]][tunnel_h] + 1
            new_value_h = value_h
            if new_time_h <= 26:
                new_value_h += rates[tunnel_h] * (26 - new_time_h)
            # the elephant moves
            new_path_e = path_e.copy()
            new_path_e.append(tunnel_e)
            new_time_e = time_e
            new_time_e += distances[path_e[-1]][tunnel_e] + 1
            new_value_e = value_e
            if new_time_e <= 26:
                new_value_e += rates[tunnel_e] * (26 - new_time_e)
            if new_time_h <= 26 or new_time_e <= 26:
                if new_value_e + new_value_h > max_value:
                    max_value = new_value_e + new_value_h
            if (
                new_time_h < 26
                and new_time_e < 26
                and set(new_path_e + new_path_h) != set(all_tunnels)
            ):
                branches.append(
                    [
                        new_path_h,
                        new_path_e,
                        new_time_h,
                        new_value_h,
                        new_time_e,
                        new_value_e,
                    ]
                )
    return max_value


def result2(myinput):
    lines = read_input(myinput)
    pre_cave = create_cave(lines)
    cave = optimize_cave(pre_cave)
    distances = all_paths(cave)
    rates, _ = cave
    value = brute_force2(distances, rates)
    return value

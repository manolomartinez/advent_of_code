from itertools import product, filterfalse
from collections import OrderedDict, defaultdict
from bisect import insort

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


## I need to parse the input more intelligently: rate 0 valves should just be
## bypassed, and the time needed to reach the following valve be 2 minutes


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


def navigate(cave):
    rates, tunnels = cave
    runs = [[set(["AA"]), "AA", [0], defaultdict(bool), 0]]
    # a set of tunnels visited so far, the last visited, a list of pressure released at each step,
    # a list of open valves, and a counter of minutes passed
    new_runs = []
    max_release = 0
    # import pdb; pdb.set_trace()
    while len(runs) > 0:
        for run in runs:
            visited, last, released, opened, minutes = run
            # print(visited)
            for tunnel in tunnels[last]:
                new_visited = visited.copy()
                new_visited.add(tunnel[0])
                new_minutes = minutes + tunnel[1]
                new_released = released + [released[-1] + release(rates, opened) * tunnel[1]]
                candidate = [new_visited, tunnel[0], new_released, opened, new_minutes]
                if not worse(candidate, new_runs):
                    if new_minutes >= 30:
                        if new_released[-1] > max_release and new_minutes == 30:
                            max_release = new_released[-1]
                            print(new_released)
                    else:
                        prev_runs = new_runs.copy()
                        new_runs = [candidate]
                        for run in prev_runs:
                            if not vet2(candidate, run):
                                new_runs.append(run)
                if rates[tunnel[0]] and not opened[tunnel[0]]:
                    new_opened = opened.copy()
                    new_opened[tunnel[0]] = True
                    new_minutes += 1
                    new_released = new_released + [
                        new_released[-1] + release(rates, opened)
                    ]
                    candidate = [
                        new_visited,
                        tunnel[0],
                        new_released,
                        new_opened,
                        new_minutes,
                    ]
                if not worse(candidate, new_runs):
                    if new_minutes >= 30:
                        if new_released[-1] > max_release and new_minutes == 30:
                            max_release = new_released[-1]
                            print(new_released)
                    else:
                        prev_runs = new_runs.copy()
                        new_runs = [candidate]
                        for run in prev_runs:
                            if not vet2(candidate, run):
                                new_runs.append(run)
        runs = new_runs
        print(len(runs))
        new_runs = []
    return max_release


def worse(candidate, runs):
    visited, last, released, opened, minutes = candidate
    for run in runs:
        if (
            visited.issubset(run[0])
            and last == run[1]
            and all(
                [
                    cand_opened <= run_opened
                    for cand_opened, run_opened in zip(opened.values(), run[3].values())
                ]
            )
            and released[-1] <= run[2][-1]
            and minutes >= run[4]
        ):
            return True
    return False


def vet2(new, old):
    visited, last, released, opened, minutes = new
    if (
        old[0].issubset(visited)
        and last == old[1]
        and all(
            [
                old_opened <= new_opened
                for old_opened, new_opened in zip(old[3].values(), opened.values())
            ]
        )
        and old[2][-1] <= released[-1]
        and old[4] >= minutes
    ):
        return True
    return False

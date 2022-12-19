from itertools import product, filterfalse
from collections import defaultdict
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
        cave[1][tunnels[0]] = tunnels[1]
    return cave


def release(rates, opened):
    total = 0
    for tunnel in rates:
        if opened[tunnel]:
            total += rates[tunnel]
    return total


def navigate(cave):
    rates, tunnels = cave
    all_tunnels = set(tunnels.keys())
    maxtunnels = len(all_tunnels)
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
                new_visited.add(tunnel)
                new_minutes = minutes + 1
                new_released = released + [released[-1] + release(rates, opened)]
                candidate = [new_visited, tunnel, new_released, opened, new_minutes]
                if not vet(new_runs, candidate):
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
                if rates[tunnel] and not opened[tunnel]:
                    new_opened = opened.copy()
                    new_opened[tunnel] = True
                    new_minutes += 1
                    new_released = new_released + [
                        new_released[-1] + release(rates, opened)
                    ]
                    candidate = [
                        new_visited,
                        tunnel,
                        new_released,
                        new_opened,
                        new_minutes,
                    ]
                if not vet(new_runs, candidate):
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


def vet(runs, candidate):
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
        # if booleans[-1]:
        # print(f"candidate: {candidate}")
        # print(f"previous: {run}")
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
        # if booleans[-1]:
    return False

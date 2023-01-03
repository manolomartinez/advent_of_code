from re import compile
from itertools import product

import numpy as np

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return np.array([parse_line(line) for line in lines])


def parse_line(line):
    p = compile(
        r"Each ore robot costs|ore. Each clay robot costs|ore. Each obsidian robot costs|ore and|clay. Each geode robot costs|ore and|obsidian."
    )
    numbers = [int(number) for number in p.split(line)[1:-1]]
    return np.array(
        [
            [numbers[0], 0, 0, 0],
            [numbers[1], 0, 0, 0],
            [numbers[2], numbers[3], 0, 0],
            [numbers[4], 0, numbers[5], 0],
        ]
    )


init_state = np.zeros(
    (1, 3, 4), dtype=int
)  # the 2nd dimension has robots, resources, time
init_state[0, 0, 0] = 1
init_state[0, 2, -1] = 24


def my_div(a, b):
    if b == 0:
        return 1000
    else:
        return a // b


vec_div = np.vectorize(my_div)


def construct_robots(resources, blueprint):
    return np.min(vec_div(resources, blueprint), axis=1)


def run_blueprint(blueprint, states=init_state, min_time=0):
    max_geodes = 0
    times_for_geodes = np.array([24] * 200)
    while len(states) > 0:
        # print(states.shape)
        robots, resources, time = states[-1].copy()
        states = states[:-1].copy()
        # possible_robots = construct_robots(resources, blueprint)
        # print(f"possible robots: {possible_robots}")
        possible_building_plans = np.all(resources >= blueprint, axis=1)
        no_robots = np.eye(4, dtype=int)[np.logical_and(possible_building_plans, np.logical_not(robots))]
        possible_building_plans = np.insert(
            possible_building_plans, 0, True, axis=0
        )
        building_plans = np.vstack(
            (np.array([0, 0, 0, 0], dtype=int), (np.eye(4, dtype=int)))
        )
        # print(resources)
        # print(building_plans)
        # print(possible_building_plans)
        # print(building_plans[possible_building_plans])
        #import pdb

        #pdb.set_trace()
        all_combinations = building_plans[possible_building_plans]
        if np.any(np.all(np.array([0, 0, 0, 1]) == all_combinations, axis=1)):
            combinations = np.array([[0, 0, 0, 1]])
            #print(resources, combinations)
        elif no_robots.shape[0] > 0:
            combinations = no_robots
        else:
            combinations = all_combinations
        for combination in combinations:
            # print(combination)
            comb_time = time.copy()
            comb_robots = robots.copy()
            comb_resources = resources.copy()
            # print(f"combination: {combination}")
            resources_for_comb = (combination.reshape(-1, 1) * blueprint).sum(0)
            # print(f"comb_resurces: {comb_resources}")
            # print(f"resources_for_comb: {resources_for_comb}")
            comb_resources -= resources_for_comb
            # print(f"resources: {resources}")
            comb_resources += comb_robots
            comb_robots += combination
            comb_time[-1] -= 1
            state = np.hstack((comb_robots, comb_resources, comb_time)).reshape(3, 4)
            if len(states) == 0:
                states = state.copy().reshape(1, 3, 4)
            else:
                remaining_time = comb_time[-1] - min_time
                if remaining_time >= 0:
                #    if not np.any(np.all(np.all(state <= states, axis=2))):
                    if comb_resources[-1] > max_geodes:
                        # print(max_geodes)
                        max_geodes = comb_resources[-1]
                        print(state)
                    if 0 < remaining_time:
                        states = np.vstack((states, state.reshape(1, 3, 4)))
                # print(f"time: {time}")
    return max_geodes


def all_blueprints(blueprints, init_robots=init_robots, init_resources=init_resources):
    geodes = []
    for blueprint in blueprints:
        _, resources = all_minutes(init_robots.copy(), init_resources.copy(), blueprint)
        print(resources)
        geodes.append(resources[-1])
    return geodes

def read_input(myfile):
    with open(myfile, 'r') as fobj:
        lines = fobj.readlines()
    return [line.split() for line in lines]


def calc_result1(myround):
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}
    points = {"X" : 1, "Y": 2, "Z": 3}
    elf, me = myround
    result = 0
    if draws[elf] == me:
        result = 3
    elif wins[elf] == me:
        result = 6
    return points[me] + result

def calc_result2(myround):
    wins = {"A": "P", "B": "S", "C": "R"}
    draws = {"A": "R", "B": "P", "C": "S"}
    loses = {"A": "S", "B": "R", "C": "P"}
    policies = {"X": loses, "Y": draws, "Z": wins}
    points1 = {"X": 0, "Y": 3, "Z": 6}
    points2 = {"R" : 1, "P": 2, "S": 3}
    elf, me = myround
    policy = policies[me]
    result = points1[me]
    result += points2[policy[elf]]
    return result

def result1(myfile):
    rounds = read_input(myfile)
    return sum(calc_result1(round) for round in rounds)

def result2(myfile):
    rounds = read_input(myfile)
    return sum(calc_result2(round) for round in rounds)

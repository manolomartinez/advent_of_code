from sys import argv

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        lines = ifile.readlines()
    return lines


# 1st star

def parse_input(lines):
    def parse_line(line):
        return np.array([int(number) for number in line[:-1].split()])
    numbers = np.array([int(number) for number in lines[0].split(sep=',')])
    cartons = []
    for line in range(1, len(lines), 6):
        carton = lines[line + 1:line + 6]
        cartons.append(np.array([parse_line(row) for row in carton]))
    return numbers, np.stack(cartons)


def booleans(cartons):
    zeros = np.zeros_like(cartons)
    return zeros.astype(bool)


def update(cartons, booleans, number):
    positions = cartons == number
    return np.logical_or(positions, booleans)


def check(booleans):
    columns = booleans.all(1)
    rows = booleans.all(2)
    bingo_col = np.where(columns)[0]
    bingo_row = np.where(rows)[0]
    bingos = list(set(list(bingo_col) + list(bingo_row)))
    if bingos:
        return bingos
    return False
    

def play (numbers, cartons):
    bools = booleans(cartons)
    for number in numbers:
        bools = update(cartons, bools, number)
        bingo = check(bools)
        if bingo:
            first = bingo[0]
            carton = cartons[first]
            for_sum = carton[np.logical_not(bools[first])]
            return number * for_sum.sum()


# 2nd star

def play_to_lose (numbers, cartons):
    bools = booleans(cartons) 
    bingos = []
    bools_when_bingo =[]
    nums_when_bingo = []
    for number in numbers:
        bools = update(cartons, bools, number)
        bingo = check(bools)
        if bingo:
            bingos.append(bingo)
            nums_when_bingo.append(number)
            bools_when_bingo.append(bools[bingo])
    how_many = [len(bingo) for bingo in bingos]
    last_pos = how_many.index(max(how_many))
    [last_carton] = list(set(bingos[last_pos]) - set(bingos[last_pos - 1]))
    carton = cartons[last_carton]
    bools = bools_when_bingo[last_pos][last_carton]
    number = nums_when_bingo[last_pos]
    for_sum = carton[np.logical_not(bools)]
    return number * for_sum.sum()


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    numbers, cartons = parse_input(data)
    # First puzzle
    result = play(numbers, cartons)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = play_to_lose(numbers, cartons)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

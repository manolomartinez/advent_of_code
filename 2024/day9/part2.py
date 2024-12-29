import numpy as np
from operator import add, mul

with open("input.txt", "r") as fo:
    input = fo.read()

parsed = [int(number) for number in input[:-1]]
gnumbers = []
gspaces = []

for index, number in enumerate(parsed):
    if index % 2:
        gspaces.append(number)
    else:
        gnumbers.append(number)

gnumbers = np.array(gnumbers)
gspaces += [0]
gspaces = np.array(gspaces)

gids = np.arange(len(gnumbers))


def move(numbers, spaces, ids, id):
    id_pos = np.where(ids == id)[0][0]
    # print("id_pos", id_pos)
    size = numbers[id_pos]
    # print("size", size)
    allslots = np.where(spaces >= size)[0]
    allslots = allslots[allslots < id_pos]
    if allslots.shape == (0,):
        return numbers, spaces, ids, id - 1
    slot = allslots[0]
    # print("slot", slot)
    numbers = np.delete(numbers, id_pos)
    numbers = np.insert(numbers, slot + 1, size)
    spaces[id_pos] += size + spaces[id_pos - 1]
    spaces = np.delete(spaces, id_pos - 1)
    spaces[slot] -= size
    spaces = np.insert(spaces, slot, 0)
    ids = np.delete(ids, id_pos)
    ids = np.insert(ids, slot + 1, id)
    return numbers, spaces, ids, id - 1


def full_run():
    numbers, spaces, ids, id = move(gnumbers, gspaces, gids, len(gids) - 1)
    while id >= 0:
        numbers, spaces, ids, id = move(numbers, spaces, ids, id)
    return numbers, spaces, ids, id


def final_calc(numbers, spaces, ids):
    mult = np.arange(sum(numbers))
    # print(mult)
    endpoints = np.cumsum(np.insert(numbers, 0, 0))
    # print(endpoints)
    mults = [mult[endpoints[i] : endpoints[i + 1]] for i in range(len(endpoints) - 1)]
    mults = list(map(add, mults, np.cumsum(np.insert(spaces, 0, 0))))
    result = list(map(mul, mults, ids))
    return sum([arr.sum() for arr in result])


print(f"Result of part 2: {final_calc(*full_run()[:-1])}")

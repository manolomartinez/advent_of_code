from itertools import product

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return [[int(number) for number in line.strip("\n")] for line in lines]


def visible(vector):
    visibles = []
    current_max = -1
    for i, tree in enumerate(vector):
        if tree > current_max:
            visibles.append(i)
            current_max = tree
    return visibles


def transpose(array):
    side = len(array)
    all_zeros = [
        [0 for _ in range(side)] for _ in range(side)
    ]  # assuming a square array
    for i, j in product(range(side), repeat=2):
        all_zeros[i][j] = array[j][i]
    return all_zeros


def sweep(array):
    side = len(array) - 1
    visibles = []
    for i, line in enumerate(array):
        left_to_right = visible(line)
        for tree in left_to_right:
            if [i, tree] not in visibles:
                visibles.append([i, tree])
        right_to_left = visible(reversed(line))
        for tree in right_to_left:
            if [i, side - tree] not in visibles:
                visibles.append([i, side - tree])
    for i, line in enumerate(transpose(array)):
        top_down = visible(line)
        for tree in top_down:
            if [tree, i] not in visibles:
                visibles.append([tree, i])
        bottom_up = visible(reversed(line))
        for tree in bottom_up:
            if [side - tree, i] not in visibles:
                visibles.append([side - tree, i])
    return visibles


def result1(myfile):
    array = read_input(myfile)
    visibles = sweep(array)
    return len(visibles)


def visible_from(array, tree):
    side = len(array) - 1
    x, y = tree
    trees_up = 0
    if x > 0:
        for tree_up in range(x - 1, -1, -1):
            trees_up += 1
            if array[tree_up][y] >= array[x][y]:
                break
    trees_down = 0
    if x < side:
        for tree_down in range(x + 1, side + 1):
            trees_down += 1
            if array[tree_down][y] >= array[x][y]:
                break
    trees_left = 0
    if y > 0:
        for tree_left in range(y - 1, -1, -1):
            trees_left += 1
            if array[x][tree_left] >= array[x][y]:
                break
    trees_right = 0
    if y < side:
        for tree_right in range(y + 1, side + 1):
            trees_right += 1
            if array[x][tree_right] >= array[x][y]:
                break
    return trees_up * trees_left * trees_right * trees_down


def result2(myfile):
    array = read_input(myfile)
    scores = []
    for x, y in product(range(len(array)), repeat=2):
        scores.append(visible_from(array, [x, y]))
    return max(scores)

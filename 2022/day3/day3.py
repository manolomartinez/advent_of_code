from itertools import islice

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return [
        [line.strip("\n")[: int(len(line) / 2)], line.strip("\n")[int(len(line) / 2) :]]
        for line in lines
    ]


def priority(line):
    item = ord(list(set(line[0]).intersection(set(line[1])))[0])
    if item >= 97:
        return item - 96
    else:
        return item - 38


def result1(myfile):
    lines = read_input(myfile)
    return sum(priority(line) for line in lines)


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError("n must be at least one")
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch


def read_input2(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return batched(lines, 3)


def priority2(group):
    item = ord(
        list(
            set(group[0].strip("\n")).intersection(
                set(group[1].strip("\n")).intersection(set(group[2].strip("\n")))
            )
        )[0]
    )
    if item >= 97:
        return item - 96
    else:
        return item - 38


def result2(myfile):
    groups = read_input2(myfile)
    return sum(priority2(group) for group in groups)

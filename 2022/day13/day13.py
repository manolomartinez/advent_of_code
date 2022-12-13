from functools import cmp_to_key
from regex import compile

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myinput):
    with open(myinput, "r") as fobj:
        content = fobj.read()
    return content


def parse_input(content):
    pairs = content.split("\n\n")
    data = []
    for pair in pairs:
        data1, data2 = pair.strip("\n").split("\n")
        data.append([eval(data1), eval(data2)])
    return data


def compare(data1, data2):
    # import pdb; pdb.set_trace()
    for el1, el2 in zip(data1, data2):
        if isinstance(el1, int) and isinstance(el2, int):
            if el1 != el2:
                return el1 < el2
        else:
            if isinstance(el1, int):
                el1 = [el1]
            if isinstance(el2, int):
                el2 = [el2]
            result = compare(el1, el2)
            if result != "draw":
                return result
    if len(data1) == len(data2):
        return "draw"
    else:
        return len(data1) < len(data2)


def result1(myinput):
    data = parse_input(read_input(myinput))
    results = [compare(*datum) * i for datum, i in zip(data, range(1, len(data) + 1))]
    return sum(results)


def parse_input2(content):
    p = compile(r"\n+")
    data = p.split(content.strip("\n"))
    return [eval(datum) for datum in data]


def comparator(data1, data2):
    if compare(data1, data2):
        return -1
    else:
        return 1


def result2(myinput):
    data = parse_input2(read_input(myinput))
    data += [[[2]], [[6]]]
    sorted_data = sorted(data, key=cmp_to_key(comparator))
    return (sorted_data.index([[2]]) + 1) * (sorted_data.index([[6]]) + 1)

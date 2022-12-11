from functools import reduce

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        myinput = fobj.read()
    raw_monkeys = myinput.split("\n\n")
    return [parse_raw_monkey(raw_monkey) for raw_monkey in raw_monkeys]


def parse_raw_monkey(raw_monkey):
    rw = raw_monkey.split("\n")
    starting = [int(item.strip(",")) for item in rw[1].split()[2:]]
    operation = eval("lambda old: " + "".join(rw[2].split()[3:]))
    divisible_by = int(rw[3].split()[-1])
    if_true = int(rw[4].split()[-1])
    if_false = int(rw[5].split()[-1])
    return [starting, operation, divisible_by, if_true, if_false, 0]


def one_round(monkeys):
    for monkey in monkeys:
        for item in monkey[0]:
            monkey[-1] += 1
            item = monkey[1](item)
            item = item // 3
            if not item % monkey[2]:
                monkeys[monkey[3]][0].append(item)
            else:
                monkeys[monkey[4]][0].append(item)
        monkey[0] = []
    return monkeys


def n_rounds(monkeys, n):
    for _ in range(n):
        monkeys = one_round(monkeys)
    return monkeys


def result1(myfile):
    monkeys = read_input(myfile)
    monkeys = n_rounds(monkeys, 20)
    inspects = [monkey[-1] for monkey in monkeys]
    most_active = sorted(inspects)[-2:]
    return most_active[0] * most_active[1]


def calc_modulo(monkeys):
    return reduce(lambda x, y: x * y, [monkey[2] for monkey in monkeys])


def one_round2(monkeys, modulo):
    for monkey in monkeys:
        for item in monkey[0]:
            monkey[-1] += 1
            item = monkey[1](item)
            item = item % modulo
            if not item % monkey[2]:
                monkeys[monkey[3]][0].append(item)
            else:
                monkeys[monkey[4]][0].append(item)
        monkey[0] = []
    return monkeys


def n_rounds2(monkeys, n, modulo):
    for _ in range(n):
        monkeys = one_round2(monkeys, modulo)
    return monkeys


def result2(myfile):
    monkeys = read_input(myfile)
    modulo = calc_modulo(monkeys)
    monkeys = n_rounds2(monkeys, 10000, modulo)
    inspects = [monkey[-1] for monkey in monkeys]
    most_active = sorted(inspects)[-2:]
    return most_active[0] * most_active[1]

from itertools import islice, count, cycle

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return [parse_line(line) for line in lines]


def parse_line(line):
    instruction = line.split()
    if len(instruction) == 2:
        return [instruction[0], int(instruction[1])]
    return instruction


def run_instruction(history, register, instruction):
    history.append(register)
    if instruction[0] == "addx":
        history.append(register)
        register += instruction[1]
    return history, register


def run_all(history, register, instructions):
    for instruction in instructions:
        history, register = run_instruction(history, register, instruction)
    return history, register


def signal_strengths(history):
    values = zip(count(20, 40), islice(history, 19, None, 40))
    return sum([value[0] * value[1] for value in values])


def result1(myfile):
    instructions = read_input(myfile)
    history, _ = run_all([], 1, instructions)
    return signal_strengths(history)


def draw_crt(history):
    display = ["." for _ in range(240)]
    for crt, register in zip(range(240), history):
        if register - 1 <= crt % 40 <= register + 1:
            display[crt] = "#"
    return display


def print_display(display):
    print(''.join(display[:40]))
    print(''.join(display[40:80]))
    print(''.join(display[80:120]))
    print(''.join(display[120:160]))
    print(''.join(display[160:200]))
    print(''.join(display[200:240]))


def result2(myfile):
    instructions = read_input(myfile)
    history, _ = run_all([], 1, instructions)
    display = draw_crt(history)
    print_display(display)



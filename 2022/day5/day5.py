# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        myinput = fobj.read()
    return myinput.split("\n\n")


def parse_stack(stack):
    columns = slice(1, 36, 4)
    lines = stack.split("\n")
    letters = [list(line[columns]) for line in lines[:-1]]
    letters.reverse()
    stacks = [[] for _ in range(9)]
    for row in letters:
        for stack, letter in zip(stacks, row):
            if letter.isalpha():
                stack.append(letter)
    return stacks


def parse_instructions(instructions):
    columns = slice(1, 6, 2)
    instructions = instructions.split("\n")[:-1]
    return [
        [int(number) for number in instruction.split()[columns]]
        for instruction in instructions
    ]


def move(instruction, stacks):
    howmany, origin, end = instruction
    for _ in range(howmany):
        crate = stacks[origin - 1].pop()
        stacks[end - 1].append(crate)
    return stacks


def result1(myfile):
    stacks, instructions = read_input(myfile)
    stacks = parse_stack(stacks)
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        move(instruction, stacks)
    return "".join([stack[-1] for stack in stacks])


def move2(instruction, stacks):
    howmany, origin, end = instruction
    crates = stacks[origin - 1][-howmany:]
    stacks[origin - 1] = stacks[origin - 1][:-howmany]
    stacks[end - 1] += crates
    return stacks


def result2(myfile):
    stacks, instructions = read_input(myfile)
    stacks = parse_stack(stacks)
    instructions = parse_instructions(instructions)
    for instruction in instructions:
        move2(instruction, stacks)
    return "".join([stack[-1] for stack in stacks])

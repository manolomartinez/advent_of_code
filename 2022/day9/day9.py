from math import copysign

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()

    return [(lambda x: [x[0], int(x[1])])(line.strip("\n").split()) for line in lines]


dirs = {"R": [0, 1], "U": [-1, 0], "L": [0, -1], "D": [1, 0]}


def move_tail(head, tail):
    new_tail = tail.copy()
    v_offset = head[0] - tail[0]
    h_offset = head[1] - tail[1]
    if abs(v_offset) <= 1 and abs(h_offset) <= 1:
        return tail
    else:
        new_tail[0] += sign_or_zero(v_offset)
        new_tail[1] += sign_or_zero(h_offset)
    return new_tail


def move_rope(head, tail, instruction, tail_positions):
    direction, times = instruction
    delta = dirs[direction]
    for _ in range(times):
        head[0] += delta[0]
        head[1] += delta[1]
        tail = move_tail(head, tail)
        if not tail in tail_positions:
            tail_positions.append(tail)
    return head, tail, tail_positions


def run_all(head, tail, instructions, tail_positions):
    for instruction in instructions:
        head, tail, tail_positions = move_rope(head, tail, instruction, tail_positions)
    return head, tail, tail_positions


def result1(myfile):
    instructions = read_input(myfile)
    _, _, tail_positions = run_all([0, 0], [0, 0], instructions, [])
    return len(tail_positions)


def sign_or_zero(number):
    if not number:
        return 0
    else:
        return int(copysign(1, number))


def move_rope2(rope, instruction, tail_positions):
    direction, times = instruction
    delta = dirs[direction]
    for _ in range(times):
        rope[0][0] += delta[0]
        rope[0][1] += delta[1]
        for i in range(1, len(rope)):
            rope[i] = move_tail(rope[i - 1], rope[i])
        if not rope[-1] in tail_positions:
            tail_positions.append(rope[-1])
    return rope, tail_positions


def run_all2(rope, instructions, tail_positions):
    for instruction in instructions:
        rope, tail_positions = move_rope2(rope, instruction, tail_positions)
    return rope, tail_positions


def result2(myfile):
    instructions = read_input(myfile)
    init_rope = [[0, 0] for _ in range(10)]
    _, tail_positions = run_all2(init_rope, instructions, [])
    return len(tail_positions)

import re

with open("input.txt", "r") as memoryfile:
    memory = memoryfile.read()

# Part 1
pattern = re.compile(r"mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)")
muls = pattern.findall(memory)
print("Part 1:", sum([eval(mul[0]) * eval(mul[1]) for mul in muls]))

# Part 2
pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d|\d\d|\d\d\d),(\d|\d\d|\d\d\d)\)")

sequence = []
enabled = True
iterator = pattern.finditer(memory)
for match in iterator:
    if match.group() == "do()":
        enabled = True
    elif match.group() == "don't()":
        enabled = False
    else:
        numbers = [eval(num) for num in match.group()[4:-1].split(",")]
        if enabled:
            sequence.append(numbers[0] * numbers[1])
print("Part 2:", sum(sequence))

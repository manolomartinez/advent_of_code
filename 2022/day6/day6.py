# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        buffer = fobj.read()
    return buffer.strip("\n")


def find_marker(buffer):
    for i in range(4, len(buffer) + 1):
        if len(set(buffer[i - 4 : i])) == 4:
            return i


def result1(myfile):
    buffer = read_input(myfile)
    return find_marker(buffer)


def find_message(buffer):
    for i in range(14, len(buffer) + 1):
        if len(set(buffer[i - 14 : i])) == 14:
            return i


def result2(myfile):
    buffer = read_input(myfile)
    return find_message(buffer)

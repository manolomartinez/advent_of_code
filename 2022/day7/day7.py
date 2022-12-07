# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return lines


def parse_input(myinput):
    instructions = []
    for line in myinput:
        words = line.strip("\n").split()
        if words[0] == "$":
            instructions.append(words[1:])
        else:
            instructions[-1].append(words)
    return instructions[1:]


class FileSystem:
    def __init__(self):
        self.dirs = set("/")  # all directories
        self.tree = {}  # children of directories
        self.tree["/"] = {}
        self.current_dir = self.tree["/"]
        self.current_path = ["/"]
        self.sizes = []

    def navigate(self):
        self.current_dir = self.tree
        for level in self.current_path:
            self.current_dir = self.current_dir[level]

    def cd(self, directory):
        directory = directory[0]
        if directory == "..":
            self.current_path.pop()
        else:
            self.current_path.append(directory)
            # self.dirs.add(self.current_path)
        self.navigate()

    def ls(self, ls_result):
        for entry in ls_result:
            if entry[0] == "dir":
                self.current_dir[entry[1]] = {}
                self.dirs.add("/".join(self.current_path) + "/" + entry[1])
            else:
                self.current_dir[entry[1]] = int(entry[0])

    def run_instruction(self, instruction):
        command_dict = {"cd": self.cd, "ls": self.ls}
        command = instruction[0]
        args = instruction[1:]
        command_dict[command](args)

    def run_all(self, instructions):
        for instruction in instructions:
            self.run_instruction(instruction)

    def dir_size(self, directory):
        if ".size" in directory:
            return directory[".size"]
        size = 0
        for item in directory:
            try:
                size += directory[item]
            except TypeError:
                size += self.dir_size(directory[item])
        directory[".size"] = size
        self.sizes.append(size)
        return size


def result1(myfile):
    lines = read_input(myfile)
    myinput = parse_input(lines)
    fs = FileSystem()
    fs.run_all(myinput)
    fs.dir_size(fs.tree["/"])
    return sum(size for size in fs.sizes if size <= 100000)


def result2(myfile):
    lines = read_input(myfile)
    myinput = parse_input(lines)
    fs = FileSystem()
    fs.run_all(myinput)
    total_size = fs.dir_size(fs.tree["/"])
    mem_needed = 30000000 - (70000000 - total_size)
    return min(size for size in fs.sizes if size >= mem_needed)

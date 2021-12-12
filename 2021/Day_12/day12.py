from sys import argv
from itertools import product, filterfalse
from collections import deque

import numpy as np


def read_input(input_file):
    with open(input_file, "r") as ifile:
        line = ifile.readlines()
    return line


# 1st star


def parse_line(line):
    return line.strip().split("-")


def parse_input(lines):
    return [parse_line(line) for line in lines]


class Graph:
    def __init__(self, lines):
        self.graph = self.build_graph(lines)
        self.nodes = list(self.graph.keys())
        self.small = [
            node
            for node in self.nodes
            if all((char.islower() for char in node)) and not node in ["start", "end"]
        ]
        self.completed_paths1 = []
        self.completed_paths2 = []

    def build_graph(self, lines):
        graph = {}
        for line in lines:
            if line[0] != "end" and line[1] != "start":
                if not line[0] in graph:
                    graph[line[0]] = [line[1]]
                else:
                    graph[line[0]].append(line[1])
            if line[1] != "end" and line[0] != "start":
                if not line[1] in graph:
                    graph[line[1]] = [line[0]]
                else:
                    graph[line[1]].append(line[0])
        return graph

    def all_paths1(self, path=["start"]):
        if path[-1] != "end":
            for node in self.graph[path[-1]]:
                if node == "end":
                    new_path = path + [node]
                    self.completed_paths1.append(new_path)
                else:
                    if node in self.small:
                        if not node in path:
                            new_path = path + [node]
                            self.all_paths1(new_path)
                    else:
                        new_path = path + [node]
                        self.all_paths1(new_path)
        return

    def can_visit(self, path, small_node):
        small_dict = {node: 0 for node in self.small}
        for node in path:
            if node in self.small:
                small_dict[node] += 1
        return (
            all([value <= 1 for value in small_dict.values()])
            or small_dict[small_node] == 0
        )

    def all_paths2(self, path=["start"]):
        if path[-1] != "end":
            for node in self.graph[path[-1]]:
                if node == "end":
                    new_path = path + [node]
                    self.completed_paths2.append(new_path)
                else:
                    if node in self.small:
                        if self.can_visit(path, node):
                            new_path = path + [node]
                            self.all_paths2(new_path)
                    else:
                        new_path = path + [node]
                        self.all_paths2(new_path)
        return


def calc_result1(graph):
    graph.all_paths1()
    return len(graph.completed_paths1)


def calc_result2(graph):
    graph.all_paths2()
    return len(graph.completed_paths2)


# 2nd star


def main():
    input_type = argv[-1] + ".txt"
    data = read_input(input_type)
    parsed_input = parse_input(data)
    graph = Graph(parsed_input)
    # First puzzle
    result = calc_result1(graph)
    print("First puzzle: {}".format(result))
    # Second puzzle
    result = calc_result2(graph)
    print("Second puzzle: {}".format(result))


if __name__ == "__main__":
    main()

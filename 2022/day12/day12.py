from itertools import product
import numpy as np

# Solutions:
# result1("input.txt")
# result2("input.txt")


def read_input(myfile):
    with open(myfile, "r") as fobj:
        lines = fobj.readlines()
    return np.array([list(line)[:-1] for line in lines])


class Problem:
    def __init__(self, elevations):
        self.elevations = elevations
        self.pos_E = self.elevations == "E"
        self.distances = np.full_like(self.elevations, 1000000, dtype=np.int32)
        self.distances[self.elevations == "S"] = 0
        self.elevations[self.elevations == "S"] = "a"
        self.elevations[self.elevations == "E"] = "z"
        self.y, self.x = self.elevations.shape
        self.neighbors = {
            point: self.calc_neighbors(point)
            for point in product(range(self.y), range(self.x))
        }
        self.check = self.neighbors.copy()

    def calc_neighbors(self, point):
        raw_neighbors = np.array(
            [
                [a, b]
                for a, b in product(
                    range(max(0, point[0] - 1), min(self.y, point[0] + 2)),
                    range(max(0, point[1] - 1), min(self.x, point[1] + 2)),
                )
            ]
        )
        neighbors = [
            tuple(raw) for raw in raw_neighbors if np.abs(point - raw).sum() == 1
        ]
        return neighbors

    def one_pass(self):
        for point in self.neighbors:
            if self.distances[point] < 1000:
                for neighbor in self.check[point]:
                    if (
                        ord(self.elevations[neighbor]) - ord(self.elevations[point])
                        <= 1
                    ):
                        self.distances[neighbor] = min(
                            self.distances[neighbor], self.distances[point] + 1
                        )
        return self.distances

    def message_passing(self):
        old_distances = np.zeros_like(self.distances)
        while np.any(old_distances != self.distances):
            old_distances = self.distances.copy()
            self.one_pass()
        return self.distances


def result1(myfile):
    elevations = read_input(myfile)
    prob = Problem(elevations)
    prob.message_passing()
    return prob.distances[prob.pos_E][0]


class Problem2:
    def __init__(self, elevations):
        self.elevations = elevations
        self.pos_E = self.elevations == "E"
        self.distances = np.full_like(self.elevations, 1000000, dtype=np.int32)
        self.distances[self.elevations == "E"] = 0
        self.elevations[self.elevations == "S"] = "a"
        self.elevations[self.elevations == "E"] = "z"
        self.y, self.x = self.elevations.shape
        self.neighbors = {
            point: self.calc_neighbors(point)
            for point in product(range(self.y), range(self.x))
        }
        self.check = self.neighbors.copy()

    def calc_neighbors(self, point):
        raw_neighbors = np.array(
            [
                [a, b]
                for a, b in product(
                    range(max(0, point[0] - 1), min(self.y, point[0] + 2)),
                    range(max(0, point[1] - 1), min(self.x, point[1] + 2)),
                )
            ]
        )
        neighbors = [
            tuple(raw) for raw in raw_neighbors if np.abs(point - raw).sum() == 1
        ]
        return neighbors

    def one_pass(self):
        for point in self.neighbors:
            if self.distances[point] < 1000:
                for neighbor in self.check[point]:
                    if (
                        ord(self.elevations[point]) - ord(self.elevations[neighbor])
                        <= 1
                    ):
                        self.distances[neighbor] = min(
                            self.distances[neighbor], self.distances[point] + 1
                        )
        return self.distances

    def message_passing(self):
        old_distances = np.zeros_like(self.distances)
        while np.any(old_distances != self.distances):
            old_distances = self.distances.copy()
            self.one_pass()
        return self.distances


def result2(myfile):
    elevations = read_input(myfile)
    prob = Problem2(elevations)
    prob.message_passing()
    return np.min(prob.distances[prob.elevations == "a"])

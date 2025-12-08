import numpy as np
from math import dist


class Point3D:
    def __init__(self, x, y, z):
        self.point = [int(x), int(y), int(z)]

    def euclidean_distance(self, other):
        return dist(self.point, other.point)

    def get_point(self):
        return self.point


def elves_day_eight_nearest_neighbor_full(input_point):
    point_pairs = [(input_point[p1], input_point[p2]) for p1 in range(len(input_point))
                   for p2 in range(p1 + 1, len(input_point))]
    circuits = {x: idx for idx, x in enumerate(input_point)}
    modified_ids = []

    prod_box = 0

    flipped_circuits = {}

    for key, value in circuits.items():
        if value not in flipped_circuits:
            flipped_circuits[value] = [key]
        else:
            flipped_circuits[value].append(key)

    while len(flipped_circuits) > 1:
        best_point1 = None
        best_point2 = None
        best_distance = np.inf
        best_idx = np.inf
        for idx, [p1, p2] in enumerate(point_pairs):
            if p1.euclidean_distance(p2) < best_distance:
                best_point1 = p1
                best_point2 = p2
                best_distance = p1.euclidean_distance(p2)
                best_idx = idx

        idx = circuits.get(best_point1)
        idx2 = circuits.get(best_point2)
        point_pairs.pop(best_idx)

        if idx != idx2:
            if idx2 not in modified_ids:
                circuits[best_point2] = idx
                modified_ids.append(idx)
            elif idx not in modified_ids:
                circuits[best_point1] = idx2
                modified_ids.append(idx2)
            else:
                for k, v in circuits.items():
                    if v == idx:
                        circuits[k] = idx2
                modified_ids.remove(idx)

        flipped_circuits = {}

        for key, value in circuits.items():
            if value not in flipped_circuits:
                flipped_circuits[value] = [key]
            else:
                flipped_circuits[value].append(key)

        if len(flipped_circuits) == 1:
            prod_box = best_point1.get_point()[0] * best_point2.get_point()[0]

    return prod_box


def elves_day_eight_nearest_neighbor(input_point, it):
    point_pairs = [(input_point[p1], input_point[p2]) for p1 in range(len(input_point))
                   for p2 in range(p1 + 1, len(input_point))]
    circuits = {x: idx for idx, x in enumerate(input_point)}
    modified_ids = []

    for i in range(it):
        best_point1 = None
        best_point2 = None
        best_distance = np.inf
        best_idx = np.inf
        if len(point_pairs) != 0:
            for idx, [p1, p2] in enumerate(point_pairs):
                if p1.euclidean_distance(p2) < best_distance:
                    best_point1 = p1
                    best_point2 = p2
                    best_distance = p1.euclidean_distance(p2)
                    best_idx = idx
            idx = circuits.get(best_point1)
            idx2 = circuits.get(best_point2)
            point_pairs.pop(best_idx)
            if idx != idx2:
                if idx2 not in modified_ids:
                    circuits[best_point2] = idx
                    modified_ids.append(idx)
                elif idx not in modified_ids:
                    circuits[best_point1] = idx2
                    modified_ids.append(idx2)
                else:
                    for k, v in circuits.items():
                        if v == idx:
                            circuits[k] = idx2
                    modified_ids.remove(idx)

    flipped_circuits = {}

    for key, value in circuits.items():
        if value not in flipped_circuits:
            flipped_circuits[value] = [key]
        else:
            flipped_circuits[value].append(key)

    first = 0
    second = 0
    third = 0

    for k, v in flipped_circuits.items():
        if len(v) > first:
            third = second
            second = first
            first = len(v)
        elif len(v) > second:
            third = second
            second = len(v)
        elif len(v) > third:
            third = len(v)

    prod_circuits = first * second * third
    return flipped_circuits, prod_circuits


if __name__ == '__main__':
    input_points = []
    with open("input.txt") as file:
        for line in file:
            x, y, z = line.strip().split(",")
            input_points.append(Point3D(x, y, z))

    """circuits, result = elves_day_eight_nearest_neighbor(input_points, 1000)
    print("The circuits are: \n")
    for k, v in circuits.items():
        print(f"The {k} group is: ")
        for val in v:
            print(val.get_point())
        print("\n")"""

    result = elves_day_eight_nearest_neighbor_full(input_points)
    print("The product is: " + str(result))

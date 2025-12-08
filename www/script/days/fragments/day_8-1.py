from decimal import Decimal
from itertools import combinations
from math import prod, sqrt

import networkx as nx


class Point():
    idx: int
    x: Decimal
    y: Decimal
    z: Decimal

    def __init__(self, idx:int, x:str, y:str, z:str) -> None:
        self.idx = idx
        self.x = Decimal(x)
        self.y = Decimal(y)
        self.z = Decimal(z)

class Edge():
    point_1: Point
    point_2: Point
    distance: Decimal

    def __init__(self, p1: Point, p2:Point) -> None:
        self.point_1 = p1
        self.point_2 = p2
        self.distance = Decimal(sqrt(
            (p1.x - p2.x)**Decimal(2)
            + (p1.y - p2.y)**Decimal(2)
            + (p1.z - p2.z)**Decimal(2)
        ))

def get_points(parsed_input: list[str]) -> list[Point]:
    points = []

    for idx, entry in enumerate(parsed_input):
       coord = entry.split(",")
       points.append(Point(idx, coord[0], coord[1], coord[2]))

    return points

def solve(parsed_input: list[str]) -> int:
    points = get_points(parsed_input)

    sorted_edges = sorted(
        [Edge(p1, p2) for p1, p2 in combinations(points, 2)],
        key=lambda x: x.distance
    )

    G= nx.Graph()

    G.add_nodes_from([point.idx for point in points])

    for i, edge in enumerate(sorted_edges):
        if i == 1000:
            return prod(sorted(map(len, nx.connected_components(G)))[-3:])
        G.add_edge(edge.point_1.idx, edge.point_2.idx)

    return 0

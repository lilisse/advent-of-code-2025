from decimal import Decimal
from itertools import combinations
from math import prod, sqrt

import matplotlib.pyplot as plt
import networkx as nx

# https://fr.wikipedia.org/wiki/Distance_euclidienne

with open("www/subjects/inputs/day_8_ex.txt", "r") as sub:
    content = sub.read()

parsed_input = content.strip().split("\n")

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
        self.closest = None
        self.closest_distance = None

    def __str__(self):
        return f"\tidx = {self.idx}\n\tx = {self.x}\n\ty = {self.y}\n\tz = {self.z}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other: Point) -> bool:
        return True if self.x == other.x and self.y == other.y and self.z == other.z else False


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

    def __str__(self) -> str:
        return f"point 1 index = {self.point_1.idx}, point 2 index = {self.point_2.idx}, distance = {self.distance}"

    def __repr__(self) -> str:
        return self.__str__()

points = []
for idx, entry in enumerate(parsed_input):
   coord = entry.split(",")
   points.append(Point(idx, coord[0], coord[1], coord[2]))

sorted_edges = sorted(
    [Edge(p1, p2) for p1, p2 in combinations(points, 2)],
    key=lambda x: x.distance
)

G= nx.Graph()

G.add_nodes_from([point.idx for point in points])


for i, edge in enumerate(sorted_edges):
    if i == 10:
        #  Pour l'exo 1
        print(prod(sorted(map(len, nx.connected_components(G)))[-3:]))
        break
    G.add_edge(edge.point_1.idx, edge.point_2.idx)
    # Pour l'exo 2
    if nx.is_connected(G):
        print(int(edge.point_1.x * edge.point_2.x))

#  Pour l'explication
# pos = nx.spring_layout(G)
# nx.draw(G, with_labels=True,pos=pos)

# plt.savefig('test.png')

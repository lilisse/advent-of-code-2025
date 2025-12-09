from itertools import combinations, compress, starmap

import matplotlib.pyplot as plt
from shapely import Polygon, box

with open("www/subjects/inputs/day_9_ex.txt", "r") as sub:
    content = sub.read()

parsed_input = content.strip().split("\n")

red_tiles = [(int(n.split(",")[0]), int(n.split(",")[1])) for n in parsed_input]

rectangles = [
    (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    for (x1, y1), (x2, y2) in combinations(red_tiles, 2)
]

rectangle_size = [
    (x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rectangles
]

print(f"{rectangles = }")
print(f"{max(rectangle_size) = }")

poly = Polygon(red_tiles)


x,y = poly.exterior.xy
print(x,y)

plt.plot(x,y)

# pour l'explication
for tile in red_tiles:
    x = tile[0]
    y = tile[1]
    print(f"x = {x}, y = {y}")
    plt.plot(x, y, marker = "^", color="red")
    plt.annotate(f"({x}, {y})", xy=(x, y), textcoords='data')

for rect in rectangles:
    print(f"{rect = }")
    print(f"{poly.contains(box(*rect)) = }")
    print()

rect_size_in_poly = compress(rectangle_size, map(poly.contains, starmap(box, rectangles)))
print(f"{max(rect_size_in_poly) = }")

plt.savefig('test.png')

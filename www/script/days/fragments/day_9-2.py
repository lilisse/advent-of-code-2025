from itertools import combinations, compress, starmap

from shapely import Polygon, box


def get_red_tiles(parsed_input: list[str]) -> list[tuple[int, int]]:
    return [(int(n.split(",")[0]), int(n.split(",")[1])) for n in parsed_input]

def solve(parsed_input: list[str]) -> int:
    red_tiles = get_red_tiles(parsed_input)

    rectangles = [
        (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
        for (x1, y1), (x2, y2) in combinations(red_tiles, 2)
    ]

    rectangle_size = [
        (x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rectangles
    ]

    return max(compress(rectangle_size, map(Polygon(red_tiles).contains, starmap(box, rectangles))))

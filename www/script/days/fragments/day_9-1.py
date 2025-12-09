from itertools import combinations


def get_red_tiles(parsed_input: list[str]) -> list[tuple[int, int]]:
    return [(int(n.split(",")[0]), int(n.split(",")[1])) for n in parsed_input]

def solve(parsed_input: list[str]) -> int:
    red_tiles = get_red_tiles(parsed_input)

    return max(
        [
            (max(x1, x2) - min(x1, x2) + 1)
            * (max(y1, y2) - min(y1, y2) + 1)
            for (x1, y1), (x2, y2) in combinations(red_tiles, 2)
        ]
    )

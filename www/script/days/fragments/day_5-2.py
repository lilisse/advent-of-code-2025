def get_fresh_and_available_ingredient(parsed_input: list[str]) -> list[list[int]]:
    return [
        [start, end]
            for item in parsed_input[:parsed_input.index("")]
            for start, end in [map(int, item.split("-"))]
        ]

def solve(parsed_input: list[str]) -> int:
    fresh = get_fresh_and_available_ingredient(parsed_input)
    interval = []

    for begin, end in sorted(fresh):
        if interval and interval[-1][1] >= begin - 1:
            interval[-1][1] = max(interval[-1][1], end)
        else:
            interval.append([begin, end])

    return sum(
        elem[1] - elem[0] + 1
        for elem in interval
    )

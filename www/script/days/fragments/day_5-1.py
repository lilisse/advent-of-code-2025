def get_fresh_and_available_ingredient(parsed_input: list[str]) -> tuple[list[range], list[int]]:
    return (
        [
            range(start, end+1)
            for item in parsed_input[:parsed_input.index("")]
            for start, end in [map(int, item.split("-"))]
        ],
        [int(num) for num in parsed_input[parsed_input.index("") + 1:]]
    )


def solve(parsed_input: list[str]) -> int:
    fresh, available = get_fresh_and_available_ingredient(parsed_input)
    return sum(
        1
        for ingredient in available
        if any(ingredient in interval for interval in fresh)
    )

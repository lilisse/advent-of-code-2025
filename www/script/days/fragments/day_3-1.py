def get_batterie_labels(parsed_input: list[str]) -> list[list[int]]:
    return [
        [int(num) for num in label]
        for label in parsed_input
    ]

def solve(parsed_input: list[str]) -> int:
    return sum(
        max(label[:-1]) * 10 + max(label[label.index(max(label[:-1])) + 1:])
        for label in get_batterie_labels(parsed_input)
    )

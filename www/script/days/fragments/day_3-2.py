def get_batterie_labels(parsed_input: list[str]) -> list[list[int]]:
    return [
        [int(num) for num in label]
        for label in parsed_input
    ]

def solve(parsed_input: list[str]) -> int:
    labels = get_batterie_labels(parsed_input)
    result = 0

    for label in labels:
        wanted_number = 12
        res = []
        while len(res) < 12:
            new_elem = max(label[:len(label)-(wanted_number - 1)])
            label = label[label.index(new_elem) + 1:]
            res.append(str(new_elem))
            wanted_number -= 1
        result += int("".join(res))

    return result

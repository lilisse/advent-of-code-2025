def process_recursive(tree: list[list[str]], idx_line: int) -> list[list[str]]:
    if idx_line >= len(tree):
        return tree

    line = tree[idx_line]
    prev_line = tree[idx_line - 1]

    for idx, char in enumerate(line):
        if char == "." and prev_line[idx] == "|":
            line[idx] = "|"
        elif (
            char == "."
            and prev_line[idx] == "^"
            and 0 < idx < len(line) - 1
        ):
            tree[idx_line - 1][idx - 1] = "|"
            tree[idx_line - 1][idx + 1] = "|"
            line[idx - 1] = "|"
            line[idx + 1] = "|"

    return process_recursive(tree, idx_line + 1)


def get_final_tree(parsed_input: list[str]) -> list[list[str]]:
    tree = []
    for line in parsed_input:
        tree.append(list(line))

    start_idx = tree[0].index("S")
    tree[1][start_idx] = "|"

    return process_recursive(tree, 2)

def solve(parsed_input: list[str]) -> int:
    final_tree = get_final_tree(parsed_input)

    return sum(
        1 for current_line in range(1, len(final_tree))
        for idx, char in enumerate(final_tree[current_line])
        if char == "^" and final_tree[current_line - 1][idx] == "|"
    )

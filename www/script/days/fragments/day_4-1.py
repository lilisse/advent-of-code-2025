def get_diagram(parsed_input: list[str]) -> list[list[str]]:
    return [list(line) for line in parsed_input]


def solve(parsed_input: list[str]) -> int:
    diagram = get_diagram(parsed_input)
    nb_rows = len(diagram)
    nb_cols = len(diagram[0]) if nb_rows > 0 else 0
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    result = 0

    for idx_rows in range(nb_rows):
        for idx_cols in range(nb_cols):
            if diagram[idx_rows][idx_cols] == ".":
                continue

            neighbours_count = 0
            for direction_rows, direction_cols in directions:
                neighbours_idx_rows = idx_rows + direction_rows
                neighbours_idx_cols = idx_cols + direction_cols

                if 0<= neighbours_idx_rows < nb_rows and 0 <=neighbours_idx_cols < nb_cols:
                    if diagram[neighbours_idx_rows][neighbours_idx_cols] == "@":
                        neighbours_count += 1

            if neighbours_count < 4:
                result += 1

    return result

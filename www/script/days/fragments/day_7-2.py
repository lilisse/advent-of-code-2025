# Calculating all possible trees takes too many resources (I tried), so I had to change
# my approach. An explanation of this approach will follow.
#
def solve(parsed_input: list[str]) -> int:
    splitters_column = [
        col
        for line in parsed_input
        for col, x in enumerate(line) if x == "^"
    ]
    beams_can_enter = [1] + [0] * (len(splitters_column) - 1)
    for idx, splitter_idx in enumerate(splitters_column):
        for prev_idx, prev_splitter_idx in enumerate(splitters_column[:idx][::-1]):
            if splitter_idx == prev_splitter_idx:
                break
            if abs(splitter_idx - prev_splitter_idx) == 1:
                beams_can_enter[idx] += beams_can_enter[idx - prev_idx - 1]

    return sum(beams_can_enter) + 1

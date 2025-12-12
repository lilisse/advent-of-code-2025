def get_regions(parsed_input: str) -> list[list[str]]:
    res = []
    for line in parsed_input.split("\n\n")[-1].split("\n"):
        size, nums = line.split(":")
        res.append(
            [
                int(size.split("x")[0]) * int(size.split("x")[1]),
                [int(num) for num in nums.strip().split(" ")]
            ]
        )
    return res


def solve(parsed_input: list[str]) -> int:
    regions = get_regions(parsed_input)
    return sum(
        1
        for region in regions
        if region[0] >= 7 * sum(map(int, region[1]))
    )

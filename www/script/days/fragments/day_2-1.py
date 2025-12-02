def get_product_ids(parsed_input: list[str]) -> list[str]:
    return [
        str(num)
        for item in parsed_input
        for start, end in [map(int, item.split("-"))]
        for num in range(start, end + 1)
    ]

def solve(parsed_input: list[str]) -> int:
    return sum(
        int(pid)
        for pid in get_product_ids(parsed_input)
        if (
            len(pid) % 2 == 0 and
            pid[:len(pid)//2] == pid[len(pid)//2:]
        )
    )

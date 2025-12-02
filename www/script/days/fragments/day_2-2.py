def get_product_ids(parsed_input: list[str]) -> list[str]:
    return [
        str(num)
        for item in parsed_input
        for start, end in [map(int, item.split("-"))]
        for num in range(start, end + 1)
    ]

def solve(parsed_input: list[str]) -> int:
    product_ids = get_product_ids(parsed_input)
    result = 0

    for pid in product_ids:
        len_pid = len(pid)
        for pattern_len in range(1, (len_pid // 2) + 1):
            if (
                len_pid % pattern_len == 0
                and pid[:pattern_len] * (len_pid // pattern_len) == pid
            ):
                result += int(pid)
                break

    return result

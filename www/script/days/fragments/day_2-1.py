def get_product_ids(parsed_input: list[str]) -> list[str]:
    return [
        str(num)
        for item in parsed_input
        for start, end in [map(int, item.split("-"))]
        for num in range(start, end + 1)
    ]

#  Raccourcire
def solve(parsed_input: list[str]) -> int:
    product_ids = get_product_ids(parsed_input)
    result = 0

    for product_id in product_ids:
        if (
            len(product_id) % 2 == 0 and
            product_id[:len(product_id)//2] == product_id[len(product_id)//2:]
        ):
            result += int(product_id)

    return result

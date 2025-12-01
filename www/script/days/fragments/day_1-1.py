def get_ope_list(parsed_input: list[str]) -> list[int]:
    result = []
    for element in parsed_input:
        if element.startswith("R"):
            result.append(int(element[1:]))
        elif element.startswith("L"):
            result.append(-int(element[1:]))
    return result

def solve(parsed_input: list[str]) -> int:
    ope_list = get_ope_list(parsed_input)
    result = 0
    pointer = 50

    for ope in ope_list:
        result += (pointer := (pointer + ope) % 100) == 0

    return result

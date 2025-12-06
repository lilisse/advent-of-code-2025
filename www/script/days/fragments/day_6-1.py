def get_problems(parsed_input: list[str]) -> tuple[list[list[int]], list[str]]:
    tmp = [
        [elem if elem in ["+", "*"] else int(elem) for elem in input.split(" ") if elem]
        for input in parsed_input
    ]
    return [list(col) for col in zip(*tmp[:-1])], tmp[-1]

def solve(parsed_input: list[str]) -> int:
    all_operands, operators = get_problems(parsed_input)
    result = 0
    for operands, operator in zip(all_operands, operators):
        res = 1 if operator == "*" else 0
        for operand in operands:
            if operator == "+":
                res += operand
            else:
                res *= operand
        result += res

    return result

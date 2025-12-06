def get_problems(parsed_input: list[str]) -> tuple[list[list[int]], list[str]]:
    operands_lines = parsed_input[:-2]
    operators_lines = parsed_input[-2]
    starts = [start for start, op in enumerate(operators_lines) if op in ["*", "+"]]
    ends = [i - 1 for i in starts[1:]] + [None]
    operators = [elem for elem in operators_lines.split(" ") if elem]
    tmp_operands = [[line[start:end] for line in operands_lines] for start, end in zip(starts, ends)]

    all_operands = []
    for operand in tmp_operands:
        res = []
        for num in zip(*operand):
            res.append(int("".join(num)))
        all_operands.append(res)

    return all_operands, operators

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

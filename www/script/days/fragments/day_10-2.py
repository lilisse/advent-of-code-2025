from z3 import Int, Optimize, Sum, sat


def get_joltages_and_buttons(parsed_input: list[str]) -> list[list[str]]:
    result = []
    for input in parsed_input:
        _, *all_buttons, joltages = input.split()
        final_joltages = list(map(int, joltages[1:-1].split(",")))
        buttons = [set(map(int, button[1:-1].split(","))) for button in all_buttons]
        result.append([final_joltages, buttons])
    return result

def solve(parsed_input: list[str]) -> int:
    joltages_and_buttons = get_joltages_and_buttons(parsed_input)

    result = 0
    for final_joltage, buttons in joltages_and_buttons:
        solver = Optimize()

        presses = [Int(f"p{idx}") for idx, _ in enumerate(buttons)]

        for press in presses:
            solver.add(press >= 0)

        for idx_jolatge, joltage in enumerate(final_joltage):
            presse_for_joltage = [
                presses[idx_button]
                for idx_button, button in enumerate(buttons)
                if idx_jolatge in button
            ]

            if presse_for_joltage:
                total_presses = Sum(presse_for_joltage)
                solver.add(total_presses == joltage)

        solver.minimize(Sum(presses))


        if solver.check() == sat:
            model = solver.model()
            result += sum(model[var].as_long() for var in model)
        else:
            print("No solutions")

    return result

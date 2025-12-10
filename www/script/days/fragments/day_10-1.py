from z3 import Int, Optimize, Sum, sat


def get_states_and_buttons(parsed_input: list[str]) -> list[list[str]]:
    result = []
    for input in parsed_input:
        states, *all_buttons, _ = input.split()
        final_states = [1 if x == "#" else 0 for x in states[1:-1]]
        buttons = [set(map(int, button[1:-1].split(","))) for button in all_buttons]
        result.append([final_states, buttons])
    return result

def solve(parsed_input: list[str]) -> int:
    states_and_buttons = get_states_and_buttons(parsed_input)

    result = 0
    for final_states, buttons in states_and_buttons:
        solver = Optimize()

        presses = [Int(f"p{idx}") for idx, _ in enumerate(buttons)]

        for press in presses:
            solver.add(press >= 0)

        for idx_state, state in enumerate(final_states):
            presse_for_state = [
                presses[idx_button]
                for idx_button, button in enumerate(buttons)
                if idx_state in button
            ]

            if presse_for_state:
                total_presses = Sum(presse_for_state)
                solver.add(total_presses % 2 == state)

        solver.minimize(Sum(presses))

        if solver.check() == sat:
            model = solver.model()
            result += sum(model[var].as_long() for var in model)
        else:
            print("No solutions")

    return result

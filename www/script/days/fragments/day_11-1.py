def get_toroidal_reactor_paths(parsed_input: list[str]) -> dict[str, list[str]]:
    return {line.split(": ")[0]: line.split(": ")[1].split(" ") for line in parsed_input}

def recursive_paths(res: dict[str, list[str]], outputs: list[str]) -> int:
    count = 0
    for output in outputs:
        if output == "out":
            count += 1
            break
        count += recursive_paths(res, res[output])
    return count

def solve(parsed_input: list[str]) -> int:
    paths = get_toroidal_reactor_paths(parsed_input)
    return recursive_paths(paths, paths["you"])

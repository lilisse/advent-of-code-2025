from functools import cache

GLOBAL = {}

def get_toroidal_reactor_paths(parsed_input: list[str]) -> dict[str, list[str]]:
    return {line.split(": ")[0]: line.split(": ")[1].split(" ") for line in parsed_input}

@cache
def recursive_paths(
    name: str,
    dac_visited: bool = False,
    fft_visited: bool = False

) -> int:
    count = 0
    dac_visited = dac_visited or name == "dac"
    fft_visited = fft_visited or name == "fft"
    if name == "out":
        count += dac_visited and fft_visited
        return count

    for output in GLOBAL["paths"][name]:
        count += recursive_paths(output, dac_visited, fft_visited)
    return count

def solve(parsed_input: list[str]) -> int:
    GLOBAL["paths"] = get_toroidal_reactor_paths(parsed_input)
    return recursive_paths("svr")

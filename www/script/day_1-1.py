from pyscript import display


def parse_input(content: str) -> list[str]:
    content_by_line = content.split("\n")
    return [str(len(content)) for content in content_by_line]

def solve(data: list[str]) -> None:
    display(" ".join(data))

solve(parse_input("bonjour\ncomment vous allez?\nau revoir\nbye"))

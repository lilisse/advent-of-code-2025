from json import load

from pyscript import display


def parse_input(content: str) -> list[str]:
    content_by_line = content.split("\n")
    return [str(len(content)) for content in content_by_line]

def display_a_file(file_name: str, target: str) -> None:
    with open(file_name, "r") as subject:
        display(subject.read(), target=target)

def display_day_name(day_number: str, target: str) -> None:
    with open("./names.json", "r") as names_files:
        names = load(names_files)
        display("Day " + str(day_number) + " - " + names[day_number], target=target)

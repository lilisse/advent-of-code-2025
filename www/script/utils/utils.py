from json import load

from pyscript import display


def get_content_of_input(file_path: str) -> str:
    with open(file_path, "r") as input_file:
        return input_file.read()

def parse_input_eol(content: str) -> list[str]:
    return content.strip().split("\n")

def parse_input_eol_without_strip(content: str) -> list[str]:
    return content.split("\n")

def parse_input_coma(input: str) -> list[str]:
    return input.strip().split(",")

def display_a_file(file_name: str, target: str) -> None:
    with open(file_name, "r") as subject:
        if file_name.endswith(".txt"):
            for line in parse_input_eol(subject.read()):
                display(line, target=target, append=True)
        else:
            display(subject.read(), target=target)

def display_day_name(day_number: str, target: str) -> None:
    with open("./names.json", "r") as names_files:
        names = load(names_files)
        display("Day " + str(day_number) + " - " + names[day_number], target=target)

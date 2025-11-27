from json import load

from pyscript import display


def display_day_name() -> None:
    with open("./config.json") as day_config_file:
        day_config = load(day_config_file)
    day_number = str(day_config.get("day_number"))

    with open("./names.json", "r") as names:
        content = load(names)
        display("Day " + day_number + " - " + content[day_number])

display_day_name()

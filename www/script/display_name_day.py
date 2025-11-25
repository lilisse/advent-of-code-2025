from json import load

from pyscript import display, document


def display_day_name() -> None:
    day_number = document.currentScript.getAttribute("day_number")
    with open("data/names.json", "r") as names:
        content = load(names)
        display("Day " + day_number + " - " + content[day_number])

display_day_name()

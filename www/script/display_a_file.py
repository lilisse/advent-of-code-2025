from pyscript import display, document


def display_a_file() -> None:
    file_name = document.currentScript.getAttribute("file_to_display")
    with open("data/" + file_name, "r") as subject:
        display(subject.read())

display_a_file()

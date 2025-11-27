from json import load

from pyscript import display, window


def display_a_file(file_name: str, target: str) -> None:
    with open(file_name, "r") as subject:
        display(subject.read(), target=target)

with open("./config.json") as day_config_file:
    day_config = load(day_config_file)

file_name_code_1 = day_config.get("code_1_file_to_display")
file_name_code_2 = day_config.get("code_2_file_to_display")
file_name_subject_1 = day_config.get("subject_1_file_to_display")
file_name_subject_2 = day_config.get("subject_2_file_to_display")

display_a_file(file_name_code_1, "code-1-1")
display_a_file(file_name_code_2, "code-1-2")
display_a_file(file_name_subject_1, "state-1-1")
display_a_file(file_name_subject_2, "state-1-2")

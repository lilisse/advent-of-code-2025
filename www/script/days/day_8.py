from day_8_1 import solve as solve_ex_1
from day_8_2 import solve as solve_ex_2
from loading import moved_progress_bar
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_8.txt")))
result_ex_2 = solve_ex_2(parse_input_eol(get_content_of_input("./input_8.txt")))


display_day_name("8", "day-title-8")
display_a_file("./day_8_1.txt", "state-8-1")
display_a_file("./day_8_1.py", "code-8-1")
display_a_file("./day_8_2.txt", "state-8-2")
display_a_file("./day_8_2.py", "code-8-2")
display(result_ex_1, target="result-8-1")
display(result_ex_2, target="result-8-2")

moved_progress_bar(8)

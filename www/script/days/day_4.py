from day_4_1 import solve as solve_ex_1
from day_4_2 import solve as solve_ex_2
from loading import moved_progress_bar
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_4.txt")))
result_ex_2 = solve_ex_2(parse_input_eol(get_content_of_input("./input_4.txt")))


display_day_name("4", "day-title-4")
display_a_file("./day_4_1.txt", "state-4-1")
display_a_file("./day_4_1.py", "code-4-1")
display_a_file("./day_4_2.txt", "state-4-2")
display_a_file("./day_4_2.py", "code-4-2")
display(result_ex_1, target="result-4-1")
display(result_ex_2, target="result-4-2")

moved_progress_bar(4)

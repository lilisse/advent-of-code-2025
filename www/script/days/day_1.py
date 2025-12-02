from day_1_1 import solve as solve_ex_1
from day_1_2 import solve as solve_ex_2
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_1.txt")))
result_ex_2 = solve_ex_2(parse_input_eol(get_content_of_input("./input_1.txt")))


display_day_name("1", "day-title-1")
display_a_file("./day_1_1.txt", "state-1-1")
display_a_file("./day_1_1.py", "code-1-1")
display_a_file("./day_1_2.txt", "state-1-2")
display_a_file("./day_1_2.py", "code-1-2")
display(result_ex_1, target="result-1-1")
display(result_ex_2, target="result-1-2")

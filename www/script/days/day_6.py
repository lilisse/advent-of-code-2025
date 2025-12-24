from day_6_1 import solve as solve_ex_1
from day_6_2 import solve as solve_ex_2
from loading import remove_loading_spinner
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
    parse_input_eol_without_strip,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_6.txt")))
result_ex_2 = solve_ex_2(parse_input_eol_without_strip(get_content_of_input("./input_6.txt")))


display_day_name("6", "day-title-6")
display_a_file("./day_6_1.txt", "state-6-1")
display_a_file("./day_6_1.py", "code-6-1")
display_a_file("./day_6_2.txt", "state-6-2")
display_a_file("./day_6_2.py", "code-6-2")
display(result_ex_1, target="result-6-1")
display(result_ex_2, target="result-6-2")

remove_loading_spinner()

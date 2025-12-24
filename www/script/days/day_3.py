from day_3_1 import solve as solve_ex_1
from day_3_2 import solve as solve_ex_2
from loading import remove_loading_spinner
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_3.txt")))
result_ex_2 = solve_ex_2(parse_input_eol(get_content_of_input("./input_3.txt")))


display_day_name("3", "day-title-3")
display_a_file("./day_3_1.txt", "state-3-1")
display_a_file("./day_3_1.py", "code-3-1")
display_a_file("./day_3_2.txt", "state-3-2")
display_a_file("./day_3_2.py", "code-3-2")
display(result_ex_1, target="result-3-1")
display(result_ex_2, target="result-3-2")

remove_loading_spinner()

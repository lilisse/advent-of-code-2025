from day_5_1 import solve as solve_ex_1
from day_5_2 import solve as solve_ex_2
from loading import remove_loading_spinner
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_5.txt")))
result_ex_2 = solve_ex_2(parse_input_eol(get_content_of_input("./input_5.txt")))


display_day_name("5", "day-title-5")
display_a_file("./day_5_1.txt", "state-5-1")
display_a_file("./day_5_1.py", "code-5-1")
display_a_file("./day_5_2.txt", "state-5-2")
display_a_file("./day_5_2.py", "code-5-2")
display(result_ex_1, target="result-5-1")
display(result_ex_2, target="result-5-2")

remove_loading_spinner()

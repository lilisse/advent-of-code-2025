from day_11_1 import solve as solve_ex_1
from day_11_2 import solve as solve_ex_2
from loading import remove_loading_spinner
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    parse_input_eol,
)

result_ex_1 = solve_ex_1(parse_input_eol(get_content_of_input("./input_11.txt")))
result_ex_2 = solve_ex_2(parse_input_eol(get_content_of_input("./input_11.txt")))


display_day_name("11", "day-title-11")
display_a_file("./day_11_1.txt", "state-11-1")
display_a_file("./explanation_day_11_1.txt", "explanation-11-1")
display_a_file("./day_11_1.py", "code-11-1")
display_a_file("./day_11_2.txt", "state-11-2")
display_a_file("./explanation_day_11_2.txt", "explanation-11-2")
display_a_file("./day_11_2.py", "code-11-2")
display(result_ex_1, target="result-11-1")
display(result_ex_2, target="result-11-2")

remove_loading_spinner()

from day_12_1 import solve as solve_ex_1
from day_12_2 import solve as solve_ex_2
from loading import remove_loading_spinner
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
    get_content_of_input,
    strip_input,
)

result_ex_1 = solve_ex_1(strip_input(get_content_of_input("./input_12.txt")))
result_ex_2 = solve_ex_2(strip_input(get_content_of_input("./input_12.txt")))


display_day_name("12", "day-title-12")
display_a_file("./day_12_1.txt", "state-12-1")
display_a_file("./day_12_1.py", "code-12-1")
display_a_file("./day_12_2.txt", "state-12-2")
display_a_file("./day_12_2.py", "code-12-2")
display(result_ex_1, target="result-12-1")
display(result_ex_2, target="result-12-2")

remove_loading_spinner()

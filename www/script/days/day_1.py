from day_1_1 import solve as solve_ex_1
from day_1_2 import solve as solve_ex_2
from pyscript import display
from utils import display_a_file, display_day_name, parse_input

result_ex_1 = solve_ex_1(parse_input("bonjour\ncomment vous allez?\nau revoir\nbye"))
result_ex_2 = solve_ex_2(
    parse_input("The\nfilesystem\nthat\nboth\nPyodide\nand\nMicroPython")
)


display_day_name("1", "day-title-1")
display_a_file("./day_1_1.txt", "state-1-1")
display_a_file("./day_1_1.py", "code-1-1")
display_a_file("./day_1_2.txt", "state-1-2")
display_a_file("./day_1_2.py", "code-1-2")
display(result_ex_1, target="result-1-1")
display(result_ex_2, target="result-1-2")

from day_2_1 import solve as solve_ex_1
from day_2_2 import solve as solve_ex_2
from pyscript import display
from utils import display_a_file, display_day_name, parse_input

result_ex_1 = solve_ex_1(
    parse_input("Host\nit\nsomewhere,\nand\ndecompress\nit\ninto\nthe\nhome\ndirectory")
)
result_ex_2 = solve_ex_2(
    parse_input("Writing\nto\na\ntext\nfile.")
)


display_day_name("2", "day-title-2")
display_a_file("./day_2_1.txt", "state-2-1")
display_a_file("./day_2_1.py", "code-2-1")
display_a_file("./day_2_2.txt", "state-2-2")
display_a_file("./day_2_2.py", "code-2-2")
display(result_ex_1, target="result-2-1")
display(result_ex_2, target="result-2-2")

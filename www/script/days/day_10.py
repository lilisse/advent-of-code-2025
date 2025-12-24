from loading import remove_loading_spinner
from pyscript import display
from utils import (
    display_a_file,
    display_day_name,
)

result_ex_1 = 469
result_ex_2 = 19293


display_day_name("10", "day-title-10")
display_a_file("./day_10_1.txt", "state-10-1")
display_a_file("./day_10_1.py", "code-10-1")
display_a_file("./day_10_2.txt", "state-10-2")
display_a_file("./day_10_2.py", "code-10-2")
display(result_ex_1, target="result-10-1")
display(result_ex_2, target="result-10-2")

remove_loading_spinner()

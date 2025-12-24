from loading import remove_loading_spinner
from pyscript import display
from utils import display_a_file

display_a_file("./utils.py", "code-utils")
display("Utils files", target="utils-title")

remove_loading_spinner()

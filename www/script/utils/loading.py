from decimal import Decimal
from time import sleep

from pyscript import document


def moved_progress_bar(step: int) -> None:
    total_script = Decimal(14)
    new_percent = round(Decimal(step + 1)* Decimal(100) / total_script, 2)
    progress_bar = document.querySelector("#loading-progress-bar")
    progress_bar.setAttribute("aria-valuenow", "nb_loaded")
    progress_bar.setAttribute("style", f"width :{new_percent}%")

    if step + 1 == total_script:
        progress_bar.setAttribute("style", f"width :{new_percent}%")
        sleep(1.5)
        document.querySelector("#progress-bar").remove()

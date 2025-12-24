from time import sleep

from pyscript import document


def remove_loading_spinner() -> None:
    sleep(0.5)
    document.querySelector("#loading-spinner").remove()

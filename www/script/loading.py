from json import load

from pyscript import document

with open("./names.json", "r") as days_name:
    days = load(days_name)

for day in days.keys():
    button = document.querySelector(f"#nav-day{day}-tab")
    if button.hasAttribute("disabled"):
        button.removeAttribute("disabled")

button = document.querySelector("#nav-utils-tab")
if button.hasAttribute("disabled"):
    button.removeAttribute("disabled")

# --- INSTRUCTIONS ---
# This script calculates a "Coder Level" based on the numbers
# the user types into the input boxes on the website.

from pyscript import document

def calculate_level(event):
    # 1. GET THE DATA
    # We look for the input boxes by their ID names
    projects_text = document.querySelector("#project-count").value
    hours_text = document.querySelector("#hours-count").value

    # We need to turn the text into numbers (integers)
    # If the box is empty, we assume 0
    if projects_text == "":
        projects = 0
    else:
        projects = int(projects_text)

    if hours_text == "":
        hours = 0
    else:
        hours = int(hours_text)

    # 2. THE LOGIC (Determine the Level)
    # CHANGE THIS: You can change the numbers to make it harder or easier!
    
    level_name = ""
    
    if projects >= 10 and hours >= 50:
        level_name = "🏆 MASTER CODER"
        color = "gold"
    elif projects >= 5 and hours >= 20:
        level_name = "🚀 ADVANCED DEVELOPER"
        color = "blue"
    elif projects >= 1:
        level_name = "🌱 JUNIOR DEVELOPER"
        color = "green"
    else:
        level_name = "🥚 NOVICE (Start Coding!)"
        color = "grey"

    # 3. SHOW THE RESULT
    # Find the header with id="level-output" and change its text
    output_box = document.querySelector("#level-output")
    output_box.innerText = "You are a: " + level_name
    output_box.style.color = color

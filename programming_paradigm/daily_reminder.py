# task_reminder.py

# Collect user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process using match-case (Python 3.10+)
match priority:
    case "high":
        message = f"🔴 High priority task: {task}"
    case "medium":
        message = f"🟠 Medium priority task: {task}"
    case "low":
        message = f"🟢 Low priority task: {task}"
    case _:
        message = f"⚪ Task: {task} (Unknown priority)"

# Modify message if time-bound
if time_bound == "yes":
    message += " — that requires immediate attention today!"

# Output the final reminder
print(message)


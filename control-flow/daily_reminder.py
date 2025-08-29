# daily_reminder.py

# Ask user for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task with match case
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = f"'{task}' has an unrecognized priority level."

# Add time sensitivity condition
if time_bound == "yes":
    reminder += " It requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."

# Print the reminder (simulate looped reminder 3 times for effect)
count = 0
while count < 3:
    print(f"Reminder: {reminder}")
    count += 1
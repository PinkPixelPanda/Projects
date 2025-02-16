import json
import os

# Load the JSON file containing task information
json_file = "tasks.json"
if not os.path.exists(json_file):
    print(f"Error: {json_file} not found in {os.getcwd()}")
    exit()

# Read task types from the JSON file
try:
    with open(json_file, "r") as file:
        task_data = json.load(file)
        task_types = task_data.get("homework_types", [])  # Extract list of task types
except json.JSONDecodeError:
    print(f"Error: {json_file} is not a valid JSON file.")
    exit()

# Define a class to store assignment type details
class TaskType:
    def __init__(self, name, display_name, tasks_per_semester, max_points_per_task):
        self.name = name
        self.display_name = display_name
        self.tasks_per_semester = tasks_per_semester
        self.max_points_per_task = max_points_per_task

# Convert task data from JSON into a list of TaskType objects
task_objects = [
    TaskType(
        task["name"],
        task["display_name"],
        task["tasks_per_semester"],
        task["max_points_per_submission"]
    ) for task in task_types
]

# Ask user for their first and last name and format it
first_name = input("What is your first name? ").title().strip()
last_name = input("What is your last name? ").title().strip()

# Print formatted greeting
print(f"\nHello, {first_name} {last_name}!\n")

# Store grades earned for each task type across multiple weeks
grades_earned = {
    "Discussion": [50, 45, 50, 50],  # Scores for each week
    "Core Assessment": [50, None, 50, None],  # None represents weeks without an assessment
    "Course Project": [50, 50, 50, 40]  # Scores for each week
}

# Calculate the maximum possible points a student can earn
max_possible_points = sum(task.tasks_per_semester * task.max_points_per_task for task in task_objects)

# Display total points earned for each assignment type
for task in task_objects:
    task_name = task.name
    max_points = task.tasks_per_semester * task.max_points_per_task
    earned_points = sum(filter(None, grades_earned.get(task_name, [])))  # Ignore None values
    print(f"Currently you have {earned_points} points for {task.display_name} out of {max_points}")

# Print the total points earned after listing individual scores
total_points = sum(filter(None, sum(grades_earned.values(), [])))
print(f"\nTotal Points Earned: {total_points}\n")

# Check if the student has achieved maximum scores in each category
for task in task_objects:
    task_name = task.name
    all_max = all(score == task.max_points_per_task for score in grades_earned.get(task_name, []) if score is not None)
    
    if all_max:
        print(f"Congrats! You got maximum points for ALL {task.display_name} homework so far!")
    else:
        print(f"Unfortunately, you did not get maximum points for ALL {task.display_name} homework.")

# Display the maximum possible grade at the very end
print(f"\nMaximum grade you can get for this class is: {max_possible_points}")

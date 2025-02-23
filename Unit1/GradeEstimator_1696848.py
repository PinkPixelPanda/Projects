import json
import os
import requests
from datetime import datetime, timezone

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
    "Discussion": [50, 45, 50, 50, 50],  # Added Week 5 grades
    "Core Assessment": [50, None, 50, None, 50],  # Added Week 5 grades
    "Course Project": [50, 50, 50, 40, 50]  # Added Week 5 grades
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

# Make a web request to World Time API
response = requests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
if response.status_code != 200:
    print("Error: Unable to retrieve time data from API.")
    exit()

# Extract time data from the JSON response
time_data = response.json()
client_ip = time_data["client_ip"]
day_of_year = time_data["day_of_year"]
utc_datetime = time_data["utc_datetime"]

# Print retrieved information
print(f"\nClient IP: {client_ip}")
print(f"Day of Year: {day_of_year}")
print(f"UTC Datetime: {utc_datetime}")

# Set course start date (January 13, 2025)
begin_course_day = datetime(2025, 1, 13).timetuple().tm_yday

# Get the current date from the API response and convert to day of the year
now_date = datetime.fromtimestamp(time_data["unixtime"], timezone.utc)
now_day = now_date.timetuple().tm_yday

# Calculate difference in days
days_elapsed = now_day - begin_course_day

# Convert days to units (1 unit = 7 days)
completed_units = days_elapsed // 7  # Integer division

# Display current unit of the class
print(f"\nYou have completed {completed_units} Units of 8.")

# Display the maximum possible grade
print(f"\nMaximum grade you can get for this class is: {max_possible_points}")

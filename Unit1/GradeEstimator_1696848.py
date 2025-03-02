import json
import os
import requests
import pandas as pd
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
        task_types = task_data.get("homework_types", [])
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

# Read grades.csv file using pandas
try:
    df = pd.read_csv("grades.csv")
    
    # Display contents of grades.csv to user
    print("CIS615 Grades:")
    print(df)
    print()
    
    # Display just the discussion grades
    print("Discussion grades:")
    discussion_row = df[df['type'] == 'discussion']
    print(discussion_row)
    print()
    
    # Display grades for Unit 1 only (week 1)
    print("Unit 1 grades:")
    unit1_grades = df.iloc[:, 1:2]  # Get week1 column
    unit1_with_type = pd.concat([df['type'], unit1_grades], axis=1)
    print(unit1_with_type)
    print()
    
    # Clean data: Cap grades at the maximum and set negative grades to 0
    cleaned_df = df.copy()

    # Define correct total possible points for each category
    max_possible_points_per_category = {
        "discussion": 400,  # 50 points per week for 8 weeks
        "core_assessment": 200,  # 50 points every other week (4 assignments)
        "course_project": 400  # 50 points per week for 8 weeks
    }

    # Cap grades at a max of 50 per assignment and set negatives to 0
    for index, row in cleaned_df.iterrows():
        task_type = row['type']
        if task_type in max_possible_points_per_category:
            for col in cleaned_df.columns[1:]:  # Skip 'type' column
                if pd.notna(cleaned_df.at[index, col]):  # Only modify existing grades
                    if cleaned_df.at[index, col] < 0:
                        cleaned_df.at[index, col] = 0  # Set negative grades to 0
                    elif cleaned_df.at[index, col] > 50:  # Max allowed per assignment
                        cleaned_df.at[index, col] = 50  # Cap grades at max

    # Display cleaned data
    print("Cleaned data:")
    print(cleaned_df)
    print()

except Exception as e:
    print(f"Error reading or processing grades.csv: {e}")
    exit()

# Compute total points earned directly from the cleaned data
total_points = cleaned_df.iloc[:, 1:].sum().sum()  

# Compute final grade percentage dynamically
final_grade = (total_points / 1000) * 100  # Since total possible points should always be 1000

# Compute actual points for each assignment type
earned_points_per_category = {
    task: cleaned_df.loc[cleaned_df['type'] == task, cleaned_df.columns[1:]].sum().sum()
    for task in max_possible_points_per_category
}

# Display total points earned
print(f"\nTotal Points Earned: {total_points:.2f}")
print(f"Your final grade percentage : {final_grade:.2f}%")

# Display total points per category
for task, max_points in max_possible_points_per_category.items():
    earned_points = earned_points_per_category[task]
    print(f"Currently you have {earned_points:.1f} points for {task.replace('_', ' ').title()} out of {max_points}")

# Check if the student has achieved maximum scores in each category
for task in max_possible_points_per_category.keys():
    all_max = all(score == 50 
                  for score in cleaned_df.loc[cleaned_df['type'] == task, cleaned_df.columns[1:]].values.flatten() if pd.notna(score))

    if all_max:
        print(f"Congrats! You got maximum points for ALL {task.replace('_', ' ').title()} homework so far!")
    else:
        print(f"Unfortunately, you did not get maximum points for ALL {task.replace('_', ' ').title()} homework.")

# Display the maximum possible grade
print(f"\nMaximum grade you can get for this class is: 1000")

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

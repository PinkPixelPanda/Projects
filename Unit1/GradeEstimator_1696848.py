# Ask user for their first name
first_name = input("What is your first name? ").title().strip()

# Ask user for their last name
last_name = input("What is your last name? ").title().strip()

# Print the full name
print(f"Hello, {first_name} {last_name}!")

# Store scores for different tasks
Unit1_discussion_points = 50  # Example discussion score
Unit1_course_project_points = 50  # Example course project score
Unit1_core_assessment_points = 50  # Example core assessment score

# Define maximum points possible per task
task_maximum_points = 50

# Calculate total points earned for Unit 1
total_points = Unit1_discussion_points + Unit1_course_project_points + Unit1_core_assessment_points

# Display total points
print(f"Total Points: {total_points}")

# Check if maximum points were achieved in each category
print("I. Got maximum points for Unit 1 discussion?", Unit1_discussion_points == task_maximum_points)
print("II. Got maximum points for Unit 1 course project?", Unit1_course_project_points == task_maximum_points)
print("III. Got maximum points for Unit 1 core assessment?", Unit1_core_assessment_points == task_maximum_points)

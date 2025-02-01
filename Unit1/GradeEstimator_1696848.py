# Using f-strings for cleaner and more readable string formatting

# Ask user for their first and last name
first_name = input("What is your first name? ").title().strip()
last_name = input("What is your last name? ").title().strip()

# Print formatted name
print(f"Hello, {first_name} {last_name}!")

# Store scores for different tasks using lists
total_discussion_points = [50, 45]  # Unit 1 and Unit 2 discussion scores
total_course_project_points = [50, 50]  # Unit 1 and Unit 2 project scores
total_core_assessment_points = [50, None]  # Unit 1 has a core assessment, Unit 2 does not

# Define the maximum points possible per task
task_maximum_points = 50  # Max score per individual assignment
discussion_max_possible = 8 * task_maximum_points  # 8 total discussions
project_max_possible = 8 * task_maximum_points  # 8 total projects
assessment_max_possible = 4 * task_maximum_points  # 4 total assessments

# Calculate total points earned so far
total_points = sum(filter(None, total_discussion_points)) + sum(total_course_project_points) + sum(filter(None, total_core_assessment_points))

# Display total points
print(f"Total Points Earned: {total_points}")

# Display formatted results for discussions, projects, and core assessments
print(f"Currently you have {sum(total_discussion_points)} points for discussions out of {discussion_max_possible}")
print(f"Currently you have {sum(total_course_project_points)} points for course projects out of {project_max_possible}")
print(f"Currently you have {sum(filter(None, total_core_assessment_points))} points for core assessments out of {assessment_max_possible}")

# Check if maximum points were achieved in each category per unit
for unit in range(len(total_discussion_points)):
    print(f"I. Got maximum points for Unit {unit+1} discussion? {total_discussion_points[unit] == task_maximum_points}")
    print(f"II. Got maximum points for Unit {unit+1} course project? {total_course_project_points[unit] == task_maximum_points}")
    
    # Handle core assessments dynamically
    if total_core_assessment_points[unit] is None:
        print(f"III. No core assessment for Unit {unit+1}")
    else:
        print(f"III. Got maximum points for Unit {unit+1} core assessment? {total_core_assessment_points[unit] == task_maximum_points}")

# Using f-strings for cleaner and more readable string formatting

# Ask user for their first and last name
first_name = input("What is your first name? ").title().strip()
last_name = input("What is your last name? ").title().strip()

# Print formatted name
print(f"\nHello, {first_name} {last_name}!\n")

# Store scores for different tasks using lists
total_discussion_points = [50, 45, 50]  # Unit 1, Unit 2, Unit 3 discussion scores
total_course_project_points = [50, 50, 50]  # Unit 1, Unit 2, Unit 3 project scores
total_core_assessment_points = [50, None, 50]  # Unit 1 had an assessment, Unit 2 did not, Unit 3 had an assessment

# Define the maximum points possible per task
task_maximum_points = 50  # Max score per individual assignment
discussion_max_possible = 8 * task_maximum_points  # 8 total discussions
project_max_possible = 8 * task_maximum_points  # 8 total projects
assessment_max_possible = 4 * task_maximum_points  # 4 total assessments

# Calculate total points earned so far
total_points = sum(total_discussion_points) + sum(total_course_project_points) + sum(filter(None, total_core_assessment_points))

# Display total points earned
print(f"Total Points Earned: {total_points}")

# Display formatted results for discussions, projects, and core assessments
print(f"Currently you have {sum(total_discussion_points)} points for discussions out of {discussion_max_possible}")
print(f"Currently you have {sum(total_course_project_points)} points for course projects out of {project_max_possible}")
print(f"Currently you have {sum(filter(None, total_core_assessment_points))} points for core assessments out of {assessment_max_possible}\n")

# Function to check if all tasks received maximum points
def check_maximum_points(grades_list, max_points, task_name):
    if all(score == task_maximum_points for score in grades_list if score is not None):
        print(f"Congrats! You got maximum points for ALL {task_name} homework so far!")
    else:
        print(f"Unfortunately, you did not get maximum points for ALL {task_name} homework.")

# Check maximum points for each category
check_maximum_points(total_discussion_points, discussion_max_possible, "discussion")
check_maximum_points(total_course_project_points, project_max_possible, "course project")
check_maximum_points(total_core_assessment_points, assessment_max_possible, "core assessment")

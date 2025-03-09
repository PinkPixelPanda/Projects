# Grade Estimator

## Overview
The **Grade Estimator** is a Python program designed to calculate a student's grade based on provided CSV files containing weekly scores for different coursework components. The program prompts the user for their name and allows them to select a data file for calculation. It then processes the data, cleans it, and computes the total earned points, final grade percentage, and letter grade.

## Features
- Reads student grades from a CSV file.
- Cleans and processes the data.
- Computes total earned points and final grade percentage.
- Provides a letter grade based on computed scores.
- Displays breakdown of scores for Discussion, Course Project, and Core Assessment.

## Prerequisites
Ensure you have the following installed on your system:
- **Python 3.x**
- **Pandas library** (install using `pip install pandas` if not already installed)

## Setup Instructions
1. Clone or download the project folder.
2. Place your CSV grade files in the same directory as the script.
3. Run the script using the following command:
   ```bash
   python3 GradeEstimator_1696848.py
   ```

## Usage
When executed, the program follows this process:
1. Prompts the user for their **first and last name**.
2. Asks the user to **choose a grade file** (e.g., `grades_0.csv` or `grades_50.csv`).
3. Reads and processes the selected file.
4. Displays **cleaned data** and calculates:
   - **Total points earned**.
   - **Final grade percentage**.
   - **Corresponding letter grade**.
   - **Breakdown of earned vs. maximum points** for each category.
5. Outputs additional details, including **maximum possible grade**, **client ID**, **day of the year**, and **UTC timestamp**.

### Example 1: Using `grades_0.csv`
```
[brittperez@Mac-5886 Unit1] % python3 GradeEstimator_1696848.py
What is your first name? Britt
What is your last name? Perez

Hello, Britt Perez!

Which file would you like to use for calculating grades? (grades_0.csv or grades_50.csv): grades_0.csv
...
Total Points Earned: 835.00
Your final grade percentage: 83.50%
Your letter grade is: B
```

### Example 2: Using `grades_50.csv`
```
[brittperez@Mac-5886 Unit1] % python3 GradeEstimator_1696848.py
What is your first name? Britt
What is your last name? Perez

Hello, Britt Perez!

Which file would you like to use for calculating grades? (grades_0.csv or grades_50.csv): grades_50.csv
...
Total Points Earned: 935.00
Your final grade percentage: 93.50%
Your letter grade is: A
```

## Sample CSV File Format
```
type,week1,week2,week3,week4,week5,week6,week7,week8
discussion,-50,45,50,50,50,50,50,0
course_project,100,50,50,40,50,50,50,0
core_assessment,50,NaN,50,NaN,50,NaN,50,NaN
```

## Notes
- `NaN` values represent missing scores and are ignored during calculation.
- The letter grade follows a standard scale:
  - **A** = 90-100%
  - **B** = 80-89%
  - **C** = 70-79%
  - **D** = 60-69%
  - **F** = Below 60%
- Users must ensure CSV files are correctly formatted before use.

## License
This project is for educational purposes and is open for modification and use.

## Author
**Britt Perez**

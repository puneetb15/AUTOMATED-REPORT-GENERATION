# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUTIONS

NAME: PUNEET BHAIRANNAVAR

INTERN ID: CT1MTIZT

DOMAIN NAME : PYTHON PROGRAMMING

BATCH DURATION: JAN 30,2025 - MAR 1,2025

# Automated Report Generation

## Overview
This project automates the process of reading data from a CSV file, analyzing it, and generating a formatted PDF report using the `reportlab` library. It is useful for creating structured reports from tabular data in an efficient manner.

## Project Structure
- **Input File**: `data.csv` (Contains employee data such as name, age, department, and salary.)
- **Output File**: `report.pdf` (Generated report containing tabular data and salary analysis.)
- **Script**: `generate_report.py` (Python script to process data and generate the PDF.)

## Prerequisites
Ensure that you have Python installed. You can check by running:
```bash
python --version
```

### Install Required Library
Install the `reportlab` library using pip:
```bash
pip install reportlab
```

## CSV File Format (`data.csv`)
Create a CSV file with sample employee data:
```csv
Name,Age,Department,Salary
John Doe,30,Engineering,75000
Jane Smith,25,Marketing,60000
Alice Johnson,35,Sales,80000
Bob Brown,40,HR,70000
```

## Script Execution (`generate_report.py`)
This Python script reads `data.csv`, calculates the average salary, and generates a PDF report.

### Running the Script
Execute the script with the following command:
```bash
python generate_report.py
```

### Expected Output
1. Reads `data.csv`.
2. Calculates the average salary.
3. Generates `report.pdf` with a tabular representation of the employee data and the computed average salary.

## Sample PDF Output Structure
```
Employee Report

Name            Age     Department      Salary
John Doe        30      Engineering     75000
Jane Smith      25      Marketing       60000
Alice Johnson   35      Sales           80000
Bob Brown       40      HR              70000

Average Salary: $71250.00
```

## Customization
- Modify the script to include additional analysis (e.g., highest/lowest salary, department-wise summary).
- Enhance PDF formatting using `reportlab.platypus` for advanced layouts.
- Integrate `matplotlib` to include visual charts and graphs.

## Contribution
Feel free to fork the repository and submit pull requests to improve the project. Suggestions and enhancements are always welcome!

## License
This project is open-source and available under the MIT License.


"""
SkillNexis Python Programming Internship - Week 4
Capstone Project: Employee Data Analysis

Features:
- Load employee data from CSV using Pandas
- Calculate average salary
- Count employees by department
- Filter employees above a salary threshold
- Export filtered results to a new CSV

Install dependency:
    pip install pandas
"""

from pathlib import Path
import pandas as pd

INPUT_FILE = "employee_dataset.csv"
OUTPUT_FILE = "employees_above_salary_threshold.csv"


def create_sample_dataset():
    """Create a sample dataset so the project can run immediately."""
    data = {
        "employee_id": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
        "name": [
            "Pavan", "Rahul", "Anjali", "Sneha",
            "Arjun", "Priya", "Kiran", "Divya"
        ],
        "department": [
            "IT", "HR", "Finance", "IT",
            "Sales", "Finance", "IT", "HR"
        ],
        "salary": [
            65000, 48000, 72000, 85000,
            55000, 68000, 92000, 51000
        ]
    }

    df = pd.DataFrame(data)
    df.to_csv(INPUT_FILE, index=False)
    print(f"Sample dataset created: {INPUT_FILE}")


def load_data():
    """Load employee records from the CSV file."""
    path = Path(INPUT_FILE)

    if not path.exists():
        create_sample_dataset()

    try:
        df = pd.read_csv(INPUT_FILE)
        return df
    except Exception as error:
        print(f"Error loading CSV: {error}")
        return None


def display_basic_analysis(df):
    """Display average salary and department employee count."""
    print("\n===== EMPLOYEE DATA ANALYSIS =====")

    average_salary = df["salary"].mean()

    print(f"Total Employees : {len(df)}")
    print(f"Average Salary  : ₹{average_salary:,.2f}")

    print("\nEmployees by Department:")
    department_count = df["department"].value_counts()

    for department, count in department_count.items():
        print(f"{department:<15} {count}")


def filter_by_salary(df):
    """Filter employees above a user-provided salary threshold."""
    while True:
        try:
            threshold = float(
                input("\nEnter salary threshold: ₹").strip()
            )

            if threshold < 0:
                print("Salary threshold cannot be negative.")
                continue

            filtered_df = df[df["salary"] > threshold].copy()

            print(
                f"\nEmployees earning more than ₹{threshold:,.2f}:"
            )

            if filtered_df.empty:
                print("No employees found above this threshold.")
            else:
                print(filtered_df.to_string(index=False))

            return filtered_df

        except ValueError:
            print("Please enter a valid numeric salary.")


def export_results(filtered_df):
    """Export filtered employee records to a new CSV file."""
    if filtered_df.empty:
        print("No records to export.")
        return

    try:
        filtered_df.to_csv(OUTPUT_FILE, index=False)
        print(f"\nResults exported successfully to: {OUTPUT_FILE}")
    except Exception as error:
        print(f"Error exporting results: {error}")


def display_menu():
    print("\n===== EMPLOYEE DATA ANALYSIS MENU =====")
    print("1. Display employee data")
    print("2. Calculate average salary")
    print("3. Department employee count")
    print("4. Filter employees by salary")
    print("5. Export filtered results")
    print("6. Run complete analysis")
    print("7. Exit")


def main():
    df = load_data()

    if df is None:
        return

    filtered_df = pd.DataFrame()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\n===== EMPLOYEE DATA =====")
            print(df.to_string(index=False))

        elif choice == "2":
            average_salary = df["salary"].mean()
            print(f"\nAverage Salary: ₹{average_salary:,.2f}")

        elif choice == "3":
            print("\n===== DEPARTMENT COUNT =====")
            print(df["department"].value_counts().to_string())

        elif choice == "4":
            filtered_df = filter_by_salary(df)

        elif choice == "5":
            if filtered_df.empty:
                print("Run salary filtering first.")
            else:
                export_results(filtered_df)

        elif choice == "6":
            display_basic_analysis(df)
            filtered_df = filter_by_salary(df)
            export_results(filtered_df)

        elif choice == "7":
            print("Exiting Employee Data Analysis Project.")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()

"""
Client Program for Project class
Estimate: 30mins
Actual:
"""
import csv
from datetime import datetime

FILENAME = "projects.txt"
from project import Project


def main():
    projects = load_projects(FILENAME)
    print(
        "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == 'L':
            projects = load_projects(FILENAME)  # Assign the loaded projects back to the 'projects' variable

        elif choice == 'S':
            save_projects(FILENAME, projects)

        elif choice == 'D':
            display_projects(projects)

        elif choice == 'F':
            date_str = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_str)

        elif choice == 'A':
            print("Let's add a new project")
            name = input("Name: ")
            start_date = datetime.strptime(input("Start date (dd/mm/yy): "), '%d/%m/%Y')
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: $"))
            completion_percentage = int(input("Percent complete: "))
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)

        else:
            print("Invalid choice. Please try again.")

        print(
            "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit")
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Loads projects from a .txt file."""
    projects = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row
        for row in reader:
            name = row[0]
            start_date = datetime.strptime(row[1], '%d/%m/%Y')  # Convert the date string to datetime
            priority = int(row[2])
            cost_estimate = float(row[3])
            completion_percentage = int(row[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    return projects


def save_projects(filename, projects):
    """Saves projects to a .txt file."""
    with open(filename, mode='w', newline='') as out_file:
        writer = csv.writer(out_file, delimiter='\t')  # Use '\t' as the delimiter
        writer.writerow(
            ["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])  # Write the header
        for project in projects:
            writer.writerow(
                [project.name, project.start_date.strftime('%d/%m/%Y'), project.priority, project.cost_estimate,
                 project.completion_percentage])


def display_projects(projects):
    """Displays current incomplete projects, sorted by priority."""
    incomplete_projects = sorted(filter(lambda x: x.completion_percentage < 100, projects), key=lambda x: x.priority)
    completed_projects = sorted(filter(lambda x: x.completion_percentage == 100, projects), key=lambda x: x.priority)

    print("Incomplete projects:")
    for i, project in enumerate(incomplete_projects, 1):
        print(
            f"{i}. {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

    print("Completed projects:")
    for i, project in enumerate(completed_projects, len(incomplete_projects) + 1):
        print(
            f"{i}. {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")


def filter_projects_by_date(projects, date_str):
    try:
        date = datetime.strptime(date_str, '%d/%m/%Y')
    except ValueError:
        print("Invalid date format. Please use 'dd/mm/yyyy' format.")
        return

    filtered_projects = [project for project in projects if project.start_date > date]
    sorted_projects = sorted(filtered_projects, key=lambda x: x.start_date)

    print(f"Projects that start after {date_str}:")
    for i, project in enumerate(sorted_projects, 1):
        print(
            f"{i}. {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, estimate: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")


if __name__ == "__main__":
    main()

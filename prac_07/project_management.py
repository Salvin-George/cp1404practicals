"""
Client Program for Project class
Estimate: 30mins
Actual:
"""
from project import Project
projects = []

print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project"
      "\n- (U)pdate project\n- (Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == 'l':
        filename = input("Enter the filename to load projects from: ")
        load_projects(filename)

    elif choice == 's':
        filename = input("Enter the filename to save projects to: ")
        save_projects(filename)

    elif choice == 'd':
        display_projects()

    elif choice == 'f':
        date_str = input("Show projects that start after date (dd/mm/yy): ")
        filter_projects_by_date(date_str)

    elif choice == 'a':
        print("Let's add a new project")
        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = int(input("Priority: "))
        cost_estimate = float(input("Cost estimate: $"))
        completion_percentage = int(input("Percent complete: "))
        project = Project(name, start_date, priority, cost_estimate, completion_percentage)
        projects.append(project)

    else:
        print("Invalid choice. Please try again.")

    print("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project"
          "\n- (U)pdate project\n- (Q)uit")
    choice = input(">>> ").upper()

print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Loads projects from a .txt file."""
    pass


def save_projects(filename):
    """Saves projects from a .txt file."""
    pass


def display_projects():
    """Displays current incomplete projects, sorted by priority."""
    pass


def filter_projects_by_date(date_str):
    """Displays projects after a certain date."""
    pass



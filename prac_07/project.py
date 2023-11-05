"""
Project Class
Estimate: 20mins
Actual:
"""
from datetime import datetime


class Project:
    """Project class object"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y')
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, start:{self.start_date}, priority:{self.priority}, estimate:{self.cost_estimate}, completion:{self.completion_percentage}"

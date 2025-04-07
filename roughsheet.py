import random

def assign_employees_to_days(employees, week_days=None):
    if week_days is None:
        week_days = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
            ]

    schedule = {}  # To store the assignment for each day

    # For each day, randomly decide if you'll assign 2 or 3 employees.
    for day in week_days:
        num_to_assign = random.choice([2, 3])
        # Make sure not to ask for more employees than available.
        if num_to_assign > len(employees):
            num_to_assign = len(employees)
        # random.sample picks unique employees for that day.
        schedule[day] = random.sample(employees, num_to_assign)
    
    return schedule

# Example usage:
employees = [
    "John Doe", "Rasheed Amolegbe", "Alice Johnson", "Michael Smith",
    "Emma Brown", "David Williams", "Sophia Martinez", "Liam Garcia",
    "Olivia Anderson", "Ethan Harris"
]

schedule = assign_employees_to_days(employees)
for day, assigned in schedule.items():
    print(f"{day}: {assigned}")

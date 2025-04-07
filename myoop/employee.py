# create an employee class
import math
import random

# Create an Employee class
class Employee:

    # class attributes
    number_of_employees = 0
    schedule = {}
    emp_list = []

    # constructor
    def __init__(self, first, last, hours = 0):
        self.first = first
        self.last = last
        self.email = (first + '.' + last +'@company.com').lower()
        self.hours = hours

        Employee.number_of_employees += 1
        self.id_number = Employee.number_of_employees

        if self.hours <= 0:
            self.number_of_working_days = 0
        else:
            self.number_of_working_days = math.ceil(self.hours / 7)
        
        self.shift_pattern = self.shift_pattern()

    
    # probab;e days of the week to work based on contracted hours
    def shift_pattern(self):
        
        week_days = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]
        
        # get tje number of working days
        days_to_work = random.sample(week_days, k = self.number_of_working_days)

        # sort the weekdays
        return sorted(days_to_work, key=week_days.index)
    
    
    def get_shift_pattern(self):
        return self.shift_pattern
    
    @classmethod
    def track_schedule(cls, instance):
        # Return the shift pattern of a single instance
        return instance.get_shift_pattern()

       
    @classmethod
    def get_global_schedule(cls, employees):
        cls.schedule = {}

        for employee in employees:
            cls.emp_list.append(employee)
            # employee_weekly_shift = Employee.track_schedule()
            employee_weekly_shift = employee.get_shift_pattern()

            for day in employee_weekly_shift:
                if day in Employee.schedule:
                    cls.schedule[day] += 1
                else:
                    cls.schedule[day] = 1
        
        return cls.schedule
        
    
    

    # def assign_employees_to_days(employees, week_days=None):
    #     if week_days is None:
    #         week_days = [
    #             'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    #             ]

    #     schedule = {}  # To store the assignment for each day

    #     # For each day, randomly decide if you'll assign 2 or 3 employees.
    #     for day in week_days:
    #         num_to_assign = random.choice([2, 3])
    #         # Make sure not to ask for more employees than available.
    #         if num_to_assign > len(employees):
    #             num_to_assign = len(employees)
    #         # random.sample picks unique employees for that day.
    #         schedule[day] = random.sample(employees, num_to_assign)
        
    #     return schedule


        


    
    # class method (alternative consstructor)
    # @classmethod
    # def from_csv(cls, file):
    #     pass

    # # static method (function a class needs but do not need to feature)
    # @staticmethod
    # def days_of_the_week():
    #     week_days = [
    #         'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
    #     ]
    #     pass


emp_1 = Employee('Rasheed', 'Amolegbe', 20)
emp_2 = Employee('Fola', 'Kayo')
emp_3 = Employee('Alice', 'Johnson', 35)
emp_4 = Employee('Michael', 'Smith', 25)
emp_5 = Employee('Emma', 'Brown', 35)
emp_6 = Employee('David', 'Williams', 35)
emp_7 = Employee('Sophia', 'Martinez', 35)
emp_8 = Employee('Liam', 'Garcia', 22)
emp_9 = Employee('Olivia', 'Anderson', 28)
emp_10 = Employee('Ethan', 'Harris', 33)
emp_11 = Employee('John', 'Doe', 35)

x = [emp_1,emp_2,emp_3,emp_4,emp_5,emp_6,emp_7,emp_8,emp_9,emp_10,emp_11]
# print(emp_1.number_of_working_days())
# print(emp_2.number_of_working_days())

print(emp_1.id_number, emp_1.number_of_working_days, emp_1.shift_pattern)
print(emp_2.id_number, emp_2.number_of_working_days, emp_2.shift_pattern)
print(emp_3.id_number, emp_3.number_of_working_days, emp_3.shift_pattern)
print(emp_4.id_number, emp_4.number_of_working_days, emp_4.shift_pattern)
print(emp_5.id_number, emp_5.number_of_working_days, emp_5.shift_pattern)
print(emp_6.id_number, emp_6.number_of_working_days, emp_6.shift_pattern)
print(emp_7.id_number, emp_7.number_of_working_days, emp_7.shift_pattern)
print(emp_8.id_number, emp_8.number_of_working_days, emp_8.shift_pattern)
print(emp_9.id_number, emp_9.number_of_working_days, emp_9.shift_pattern)
print(emp_10.id_number, emp_10.number_of_working_days, emp_10.shift_pattern)
print(emp_11.id_number, emp_11.number_of_working_days, emp_11.shift_pattern)

print()
print(Employee.get_global_schedule(x))

      
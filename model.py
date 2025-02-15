import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
import random

# class Employee:
#     def __init__(self, id, salary):
#         self.id = id
#         self.salary = salary

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary


class Company:
    def __init__(self, starting_employees, starting_capital, salary = 1):
        self.num_employees = starting_employees
        # self.revenue_per_employee = revenue_per_employee
        self.cash = starting_capital  # Initial cash
        self.salary = salary

    def pay_salaries(self):
        total_paychecks = self.num_employees * self.salary
        self.cash -= total_paychecks
        # print(f"Step {self.time_step}: Paid ${total_salaries} in salaries")

    def earn_revenue(self):
        revenue = len(self.employees) * self.revenue_per_employee
        self.cash += revenue
        print(f"Step {self.time_step}: Earned ${revenue} in revenue")

    def hire_employee(self, salary):
        new_employee = Employee(len(self.employees), salary)
        self.employees.append(new_employee)
        print(f"Step {self.time_step}: Hired Employee {new_employee.id}")

    def fire_employee(self):
        if self.employees:
            fired_employee = self.employees.pop()
            print(f"Step {self.time_step}: Fired Employee {fired_employee.id}")

    def simulate_step(self):
        self.time_step += 1
        self.earn_revenue()
        self.pay_salaries()

        # Example decision logic: Hire if cash is high, fire if cash is low
        if self.cash > 200000:
            self.hire_employee(5000)
        elif self.cash < 50000 and self.employees:
            self.fire_employee()

        print(f"Step {self.time_step}: Cash Balance: ${self.cash}")

class Simulation:
    def __init__(self, company, steps):
        self.company = company
        self.steps = steps

    def run(self):
        for _ in range(self.steps):
            self.company.simulate_step()
            print("="*30)

# Example Run
company = Company(starting_employees=10, base_salary=5000, revenue_per_employee=7000)
sim = Simulation(company, steps=10)
sim.run()
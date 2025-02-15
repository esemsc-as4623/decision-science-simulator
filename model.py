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
    def __init__(self, starting_employees, starting_capital, salary = 1, age=0, alive=True):
        self.num_employees = starting_employees
        # self.revenue_per_employee = revenue_per_employee
        self.cash = starting_capital  # Initial cash
        self.salary = salary
        self.age = age
        self.alive = alive

    def pay_salaries(self):
        total_paychecks = self.num_employees * self.salary

        if total_paychecks > self.cash:
            self.die()
            return
        self.cash -= total_paychecks
        print(f'Paid {self.num_employees * self.salary} paycheck{'s' if self.num_employees > 1 else ''} in salaries')

    def die(self):
        self.alive = False
    # def earn_revenue(self):


    # def hire_employee(self, salary):


    # def fire_employee(self):

class Simulation:
    def __init__(self, company, max_steps=50):
        self.company = company
        self.max_steps = max_steps

    def run(self):
        time_step=0
        steps = []
        employees = []
        cash = []
        while company.alive and time_step < self.max_steps:
            employees.append(company.num_employees)
            cash.append(company.cash)
            steps.append(time_step)
            company.pay_salaries()
            time_step += 1
            company.age += 1
        
        dead_alive = ['dead', 'alive']
        print(f'At the end of {time_step - 1} steps, the company is {dead_alive[company.alive]}')
        return steps, employees, cash

# Example Run
company = Company(starting_employees=2, starting_capital=10)
sim = Simulation(company, max_steps=50)
a, b, c = sim.run()
print(c)
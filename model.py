import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time
import random

# class Employee:
#     def __init__(self, id, salary):
#         self.id = id
#         self.salary = salary

class Product:
    def __init__(self, users, subscription_price=1):
        self.users = users
        self.subscription_price = subscription_price

    def user_increase(self, delta_t):
        self.users += 1 * delta_t # linear for now
    
    def collect_subscriptions(self):
        return self.users * self.subscription_price

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

class Company:
    def __init__(self, starting_employees, starting_capital, salary = 500, age=0,
                 alive=True, users=0, subscription_price= 1):
        self.num_employees = starting_employees
        # self.revenue_per_employee = revenue_per_employee
        self.cash = starting_capital  # Initial cash
        self.salary = salary
        self.age = age
        self.alive = alive
        self.products = []
        self.products.append(Product(users, subscription_price))

    def pay_salaries(self):
        total_paychecks = self.num_employees * self.salary

        if total_paychecks > self.cash:
            self.die()
            return
        self.cash -= total_paychecks
        print(f'Paid {self.num_employees * self.salary} paycheck{"s" if self.num_employees > 1 else ""} in salaries')

    def earn_revenue(self):
        total_revenue = 0
        for product in self.products:
            total_revenue += product.collect_subscriptions()
        self.cash += total_revenue
        print(f'Earned {total_revenue} in revenue')

    def die(self):
        self.alive = False

class Simulation:
    def __init__(self, company, step_size=1, max_steps=50):
        self.company = company
        self.max_steps = max_steps
        self.step_size = step_size

    def run(self):
        time_step=0
        steps = []
        employees = []
        cash = []
        while self.company.alive and time_step < self.max_steps:

            employees.append(self.company.num_employees)
            cash.append(self.company.cash)
            steps.append(time_step)

            self.company.earn_revenue()
            self.company.pay_salaries()
            for product in self.company.products:
                product.user_increase(self.step_size)

            time_step += self.step_size
            self.company.age += 1
        
        dead_alive = ['dead', 'alive']
        print(f'At the end of {time_step - 1} steps, the company is {dead_alive[self.company.alive]}')
        return steps, employees, cash

# Example Run
company = Company(starting_employees=3, starting_capital=5000)
sim = Simulation(company, max_steps=50)
a, b, c = sim.run()
print(c)
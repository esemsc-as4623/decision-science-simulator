import numpy as np

def sigmoid(x):
    return 250 / (1 + np.exp(-x+6))

def exponential(x):
    return np.exp(x)

class Product:
    def __init__(self, users, subscription_price=1):
        self.users = users
        self.subscription_price = subscription_price

    def user_increase(self, delta_t, lbda):
        self.users += delta_t * lbda  # linear for now
    
    def collect_subscriptions(self):
        return self.users * self.subscription_price

class Cost_of_Inaction:
    def __init__(self, cost=1, t=0):
        self.cost = cost
        self.t = t

    def cost_increase(self, delta_t):
        self.cost += delta_t * np.exp(self.t)
        self.t += delta_t

    def cost_decrease(self, delta_t):
        self.cost -= delta_t * np.exp(self.t)
        self.t -= delta_t

class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

class Company:
    def __init__(self, starting_employees, starting_capital, salary, age=0,
                 alive=True, users=0, subscription_price= 1):
        self.num_employees = starting_employees
        # self.revenue_per_employee = revenue_per_employee
        self.cash = starting_capital  # Initial cash
        self.salary = salary
        self.age = age
        self.alive = alive
        self.products = []
        self.products.append(Product(users, subscription_price))
        self.inaction = Cost_of_Inaction(0)

    def add_employee(self):
        self.num_employees += 1
        print(f'Hired an employee. Total employees: {self.num_employees}')

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

    def invest(self, delta_t=1):
        self.cash -= max(int(self.inaction.cost),0)
        self.inaction.cost_decrease(delta_t)

    def die(self):
        self.alive = False

class Simulation:
    def __init__(self, company, step_size=1, max_steps=50, probs_sustainability=0.5):
        self.company = company
        self.max_steps = max_steps
        self.step_size = step_size
        self.probs = [probs_sustainability, 1 - probs_sustainability]

    def run(self):
        time_step=0
        steps = []
        employees = []
        cash = []
        while self.company.alive and time_step < self.max_steps:

            employees.append(self.company.num_employees)
            cash.append(self.company.cash)
            steps.append(time_step)

            step_action = np.random.choice([0,1], p=self.probs)

            if step_action == 1:
                self.company.add_employee()
            else:
                self.company.invest(self.step_size)

            self.company.earn_revenue()
            self.company.pay_salaries()

            increase_coeff = int(sigmoid(self.company.num_employees))
            # print(f'Number of employees: {self.company.num_employees}')
            # print(f'Increase coefficient: {increase_coeff}')

            for product in self.company.products:
                product.user_increase(self.step_size, increase_coeff)

            self.company.inaction.cost_increase(self.step_size)

            if self.company.cash < self.company.inaction.cost:
                self.company.die()
                print(f'Dying from not listening to Greta. The cost would be {self.company.inaction.cost}')

            time_step += self.step_size
            self.company.age += 1
        
        dead_alive = ['dead', 'alive']
        print(f'At the end of {time_step - 1} steps, the company is {dead_alive[self.company.alive]}')
        return steps, employees, cash

# # Example Run
# company = Company(starting_employees=1, starting_capital=10000)
# sim = Simulation(company, max_steps=50)
# a, b, c = sim.run()
# print(c)

# # probs=np.linspace(0, 1, 3)

# # lifetimes = []

# # for prob in probs:
# #     company = Company(starting_employees=1, starting_capital=10000)
# #     sim = Simulation(company, max_steps=50, probs_sustainability=prob)
# #     steps, _, _ = sim.run()
# #     lifetimes.append(len(steps))

# # print(lifetimes)
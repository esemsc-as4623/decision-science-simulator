from model import Company, Simulation
from animator import plot_animation
import matplotlib.pyplot as plt
import time

def read_config():
    with open("config.txt", "r") as f:
        lines = f.readlines()
        n_employees = int(lines[0].split(":")[1].strip())
        n_capital = int(lines[1].split(":")[1].strip())
        age = int(lines[2].split(":")[1].strip())
    return n_employees, n_capital, age

def main():
    # Read initial conditions
    n_employees, n_capital, max_time = read_config()
    
    # Initialize company and simulation
    company = Company(starting_employees=1,
                      starting_capital=10,
                      salary=1)
    # company = Company(3, 10)
    simulation = Simulation(company, max_steps=10)
    
    # Run simulation with animation
    age, employees, capital = simulation.run()
    print(capital, employees, age)
    plot_animation(capital, employees, age)

if __name__ == "__main__":
    main()

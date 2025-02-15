from model import Company, Simulation
from animator import plot_animation
import os

def read_config(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        n_employees = int(lines[0].split(":")[1].strip())
        n_capital = int(lines[1].split(":")[1].strip())
        age = int(lines[2].split(":")[1].strip())
    return n_employees, n_capital, age


def main():
    for file in os.listdir("cases"):
        # Read initial conditions
        n_employees, n_capital, max_time = read_config(f"cases/{file}")
        # Initialize company and simulation
        company = Company(starting_employees=n_employees,
                        starting_capital=n_capital)
        # company = Company(3, 10)
        simulation = Simulation(company, max_steps=max_time)
        
        # Run simulation with animation
        age, employees, capital = simulation.run()
        print(capital, employees, age)
        plot_animation(capital, employees, age, save_as=file.split(".")[0])

if __name__ == "__main__":
    main()

from model import Company, Simulation
from animator import plot_grid
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
    # company = Company(n_employees, n_capital)
    company = Company(3, 10)
    simulation = Simulation(company, max_time)
    
    # Set up interactive plotting
    plt.ion()
    
    # Run simulation with animation
    for _ in range(max_time):
        age, employees, capital = simulation.run()
        print(age, employees, capital)
        plot_grid(capital, employees, age)
        time.sleep(0.5)  # Add delay between frames
        
    # Keep the final plot visible
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    main()

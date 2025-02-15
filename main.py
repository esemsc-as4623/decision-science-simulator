from model import Company, Simulation
from animator import plot_grid

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
    company = Company(n_employees, n_capital)
    plot_grid(company)

if __name__ == "__main__":
    main()

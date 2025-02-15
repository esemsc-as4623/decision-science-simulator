import numpy as np
import matplotlib.pyplot as plt
import time

def read_config():
    with open("config.txt", "r") as f:
        lines = f.readlines()
        n_employees = int(lines[0].split(":")[1].strip())
        n_capital = int(lines[1].split(":")[1].strip())
        age = int(lines[2].split(":")[1].strip())

    return n_employees, n_capital, age

def plot_grid(num_colored, n_employees, age, grid_size=(5, 5), seed=42):
    np.random.seed(seed)

    # Create figure with custom size and two subplots
    fig = plt.figure(figsize=(12, 8))
    
    # Create two subplots: one for the grid (left) and one for text (right)
    grid_ax = plt.subplot(121)  # 1 row, 2 cols, position 1
    text_ax = plt.subplot(122)  # 1 row, 2 cols, position 2

    # Plot grid in the left subplot
    grid = np.zeros(grid_size)
    total_squares = grid_size[0] * grid_size[1]
    positions = np.random.choice(total_squares, num_colored, replace=False)
    
    for pos in positions:
        row = pos // grid_size[1]
        col = pos % grid_size[1]
        grid[row, col] = 1
    
    grid_ax.pcolormesh(grid, cmap=plt.cm.colors.ListedColormap(['white', 'blue']), shading='flat')
    grid_ax.grid(True)
    grid_ax.axis('equal')
    grid_ax.axis('off')
    grid_ax.set_title('Remaining Capital')

    # Add text in the right subplot
    text_ax.text(0.1, 0.6, f't = {age}\ncurrent employees = {n_employees}', 
                 fontsize=12, verticalalignment='center')
    text_ax.axis('off')  # Hide axes for text subplot

    plt.show()

if __name__ == "__main__":
    n_employees, n_capital, age = read_config()
    plot_grid(n_capital, n_employees, age)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_grid(num_colored, text="", grid_size=(10, 10), seed=42):
    plt.clf()  # Clear the current figure
    
    total_squares = grid_size[0] * grid_size[1]
    if num_colored > total_squares:
        # Calculate minimum grid size needed based on num_colored
        min_side = int(np.ceil(np.sqrt(num_colored)))  # Square root rounded up
        grid_size = (min_side, min_side)  # Make a square grid

    # Create two subplots: one for the grid (left) and one for text (right)
    grid_ax = plt.subplot(121)
    text_ax = plt.subplot(122)

    # Plot grid in the left subplot
    grid = np.zeros(grid_size)
    
    if num_colored > 0:
        positions = np.arange(num_colored)
        
        for pos in positions:
            row = pos // grid_size[1]
            col = pos % grid_size[1]
            grid[row, col] = 1
    
    grid_ax.pcolormesh(grid, cmap=plt.cm.colors.ListedColormap(['white', 'blue']), shading='flat')
    # Add these lines to show major gridlines
    grid_ax.set_xticks(np.arange(grid.shape[1]+1), minor=False)
    grid_ax.set_yticks(np.arange(grid.shape[0]+1), minor=False)
    grid_ax.grid(True, which='major', color='white', linewidth=2)
    grid_ax.set_axisbelow(False)
    grid_ax.set_xticklabels([])  # Remove x-axis tick labels
    grid_ax.set_yticklabels([])  # Remove y-axis tick labels
    grid_ax.set_aspect('equal', adjustable='box')
    grid_ax.set_title('Remaining Capital')

    # Add text in the right subplot
    text_ax.text(0.1, 0.6, text,
                 fontsize=12, verticalalignment='center')
    text_ax.axis('off')

def plot_animation(capital, employees, steps):
    assert len(capital) == len(employees) == len(steps), "All inputs must have the same length"

    plt.ion()
    fig = plt.figure(figsize=(12, 8))
    
    try:
        ani = FuncAnimation(
            fig, 
            lambda i: plot_grid(capital[i], f"t = {steps[i]}\nCurrent employees = {employees[i]}\nCapital = {capital[i]}"),
            frames=len(capital),
            interval=500
        )
        
        # Save as GIF
        ani.save("simulation.gif", fps=2)
    finally:
        plt.close()

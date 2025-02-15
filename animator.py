import numpy as np
import matplotlib.pyplot as plt

def plot_grid(num_colored, text="", grid_size=(5, 5), seed=42):
    np.random.seed(seed)

    # Create figure with custom size and two subplots
    fig = plt.figure(figsize=(12, 8))
    
    # Create two subplots: one for the grid (left) and one for text (right)
    grid_ax = plt.subplot(121)
    text_ax = plt.subplot(122)

    # Plot grid in the left subplot
    grid = np.zeros(grid_size)
    total_squares = grid_size[0] * grid_size[1]
    
    # Ensure num_colored doesn't exceed total squares
    num_colored = min(max(0, num_colored), total_squares)  # Clamp between 0 and total_squares
    
    if num_colored > 0:  # Only try to choose positions if we need colored squares
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
    text_ax.text(0.1, 0.6, text,
                 fontsize=12, verticalalignment='center')
    text_ax.axis('off')

    plt.show()

def plot_animation(capital, employees, steps):
    assert len(capital) == len(employees) == len(steps), "All inputs must have the same length"

    try:
        plt.ion()  # Enable interactive mode
        for i in range(len(capital)):
            plot_grid(capital[i], f"t = {steps[i]}\nCurrent employees = {employees[i]}")
            plt.pause(0.5)
            plt.clf()  # Clear the plot for the next iteration
    except Exception as e:
        print(e)

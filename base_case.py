


def cookie():

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    import time
    # Parameters
    initial_employees = 1
    initial_paychecks = 10
    paycheck_cost = 1
    revenue_mean = 3
    revenue_std = 2
    time_steps = 50
    cookie_integrity = 100
    cookie_decay_rate = 10

    # State variables
    employees = initial_employees
    paychecks = initial_paychecks
    cookie_integrity_history = []
    cookie_integrity = 100

    # Visualization setup
    fig, ax = plt.subplots(figsize=(6, 6))

    for t in range(time_steps):
        revenue = max(0, np.random.normal(revenue_mean, revenue_std))
        expenses = employees * paycheck_cost
        paychecks += revenue - expenses

        if paychecks < 0:  # Lay off employees if we run out of money
            employees = max(0, employees - 1)
            cookie_integrity -= cookie_decay_rate
        elif paychecks > expenses + paycheck_cost:  # Hire if we have extra savings
            employees += 1

        cookie_integrity = max(0, cookie_integrity)
        cookie_integrity_history.append(cookie_integrity)

        # Clear plot
        ax.clear()
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.set_aspect('equal')
        ax.axis('off')

        # Draw cookie
        cookie = patches.Circle((0, 0), radius=1, facecolor='peru', edgecolor='saddlebrown')
        ax.add_patch(cookie)

        # Bite marks based on cookie integrity
        bite_count = (100 - cookie_integrity) // 20
        bite_positions = [(0.7, 0.7), (-0.8, 0.6), (0.8, -0.7), (-0.6, -0.8), (0, 1)]
        for i in range(min(bite_count, len(bite_positions))):
            bite = patches.Circle(bite_positions[i], radius=0.3, facecolor='white', edgecolor='white')
            ax.add_patch(bite)

        # Display current state
        ax.text(-1, -1.3, f"Employees: {employees}\nPaychecks: {paychecks:.2f}\nCookie Integrity: {cookie_integrity}", fontsize=10)

        plt.pause(0.5)

    plt.show()

def grid():
    import numpy as np
    import matplotlib.pyplot as plt
    import time

    # Parameters
    initial_employees = 1
    initial_paychecks = 10
    paycheck_cost = 1
    revenue_mean = 3
    revenue_std = 2
    time_steps = 50
    cookie_integrity = 100
    cookie_decay_rate = 10

    # State variables
    employees = initial_employees
    paychecks = initial_paychecks
    cookie_integrity_history = []
    cookie_integrity = 100

    # Visualization setup
    grid_size = 10
    cookie_grid = np.ones((grid_size, grid_size))

    # Helper function to degrade the cookie
    def degrade_cookie(grid, integrity):
        bites = (100 - integrity) // 10
        for _ in range(bites):
            x, y = np.random.randint(0, grid_size, size=2)
            grid[x, y] = 0

    for t in range(time_steps):
        revenue = max(0, np.random.normal(revenue_mean, revenue_std))
        expenses = employees * paycheck_cost
        paychecks += revenue - expenses

        if paychecks < 0:  # Lay off employees if we run out of money
            employees = max(0, employees - 1)
            cookie_integrity -= cookie_decay_rate
        elif paychecks > expenses + paycheck_cost:  # Hire if we have extra savings
            employees += 1

        cookie_integrity = max(0, cookie_integrity)
        cookie_integrity_history.append(cookie_integrity)

        degrade_cookie(cookie_grid, cookie_integrity)

        # Clear plot
        plt.clf()
        plt.imshow(cookie_grid, cmap="Oranges", vmin=0, vmax=1)
        plt.title(f"Time: {t}\nEmployees: {employees}\nPaychecks: {paychecks:.2f}\nCookie Integrity: {cookie_integrity}")
        plt.axis('off')

        plt.pause(0.5)

    plt.show()


# cookie()

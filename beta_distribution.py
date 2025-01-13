import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.special import beta

# Beta PDF function
def beta_pdf(x, a, b):
    return x**(a-1) * (1-x)**(b-1) / beta(a, b)

# Set up the figure and axis
fig, ax = plt.subplots()
x = np.linspace(0, 1, 1000)
line, = ax.plot([], [], lw=2)

# Generate a_b_pairs for the "back-and-forth" animation
a_b_pairs = [(a, b) for a in range(1, 10) for b in range(2, 3)]

# Initialize the plot
def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 10)
    ax.set_title("Beta Distribution Animation")
    ax.set_xlabel("X")
    ax.set_ylabel("Density")
    return line,

# Update the plot for each frame
def update(frame):
    # Select the current (a, b) pair based on the frame index
    a, b = a_b_pairs[frame % len(a_b_pairs)]  # Cycle through the list
    y = [beta_pdf(xi, a, b) for xi in x]  # Calculate PDF for current (a, b)
    line.set_data(x, y)  # Update the line plot
    ax.set_title(f"Beta PDF (a={a}, b={b})")  # Update the title
    return line,

def plot_beta():
    # Create the animation, one frame per (a, b) pair
    ani = FuncAnimation(fig, update, frames=len(a_b_pairs), init_func=init, blit=True)

    # Display the animation
    plt.show()

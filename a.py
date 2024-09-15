import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Setting up the figure, the axis, and the plot elements.
fig, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 300)
line, = ax.plot(x, np.sin(x))

def init():
    """Initialize the line data for the animation."""
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

def animate(i):
    """Update the line data for each frame of the animation."""
    line.set_ydata(np.sin(x + i/10.0))  # Update the y data with a changing frequency.
    return line,

# Setting the animation parameters.
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=50, blit=True)

plt.ylim(-2, 2)  # Set the y-axis limits.
plt.title("Sine Wave Animation")
plt.show()

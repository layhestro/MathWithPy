import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the Gaussian function
def gaussian(x):
  return np.exp(-x**2)

# Define its Fourier transform
def fourier_transform_gaussian(frequency):
  return np.exp(-np.pi*frequency**2)

x = np.linspace(-5, 5, 400)
frequencies = np.linspace(-2, 2, 400)

# Prepare the figure and axes
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Plot the Gaussian on the first subplot
ax1.plot(x, gaussian(x), label='Original Function - Gaussian', color='blue')
line1, = ax1.plot(x, 0 * gaussian(x), color='red', label='Sinusoid at frequency f')
ax1.set_ylim(-1.2, 1.2)
ax1.legend()
ax1.set_title('Original Function and Sinusoid')
ax1.grid(True)

# Plot the Fourier transform magnitude on the second subplot
ax2.plot(frequencies, fourier_transform_gaussian(frequencies), label='Fourier Transform', color='blue')
line2, = ax2.plot([], [], 'ro', markersize=5, label='Current Frequency Magnitude')
ax2.set_ylim(0, 1.2)
ax2.legend()
ax2.set_title('Fourier Transform Magnitude')
ax2.grid(True)

def animate(frequency):
    sinusoid = np.cos(2*np.pi*frequency*x)
    line1.set_ydata(sinusoid)
    line1.set_label(f'Sinusoid at frequency {frequency:.2f}')
    line2.set_data(frequency, fourier_transform_gaussian(frequency))
    ax1.legend()

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(-2, 2, 100), repeat=False)

plt.tight_layout()
plt.show()
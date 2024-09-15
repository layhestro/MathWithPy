import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the domain
x = np.linspace(-10, 10, 1000)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Initial plots
line1, = ax[0].plot(x, np.exp(-x**2 / (2 * 1**2)), 'b-')
ax[0].set_title('Gaussian Function')
ax[0].set_xlabel('x')
ax[0].set_ylabel('Amplitude')
ax[0].set_ylim([-0.1, 1.1])
ax[0].grid(True)

frequencies = np.fft.fftfreq(x.size, d=x[1]-x[0])
yf_initial = np.abs(np.fft.fftshift(np.fft.fft(np.exp(-x**2 / (2 * 1**2)))))
line2, = ax[1].plot(frequencies, yf_initial, 'b-')
ax[1].set_title('Magnitude of Fourier Transform')
ax[1].set_xlabel('Frequency')
ax[1].set_ylabel('Magnitude')
ax[1].set_xlim([-5, 5])
ax[1].grid(True)

def animate(std_dev):
    y = np.exp(-x**2 / (2 * std_dev**2))
    line1.set_ydata(y)

    yf = np.abs(np.fft.fftshift(np.fft.fft(y)))
    line2.set_ydata(yf)
    line2.set_ylim([0, yf.max()+5])

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0.5, 3, 60), repeat=False)

plt.tight_layout()
plt.show()

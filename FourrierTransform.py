import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fs = 1000  # Sampling frequency
t = np.arange(0, 2, 1/fs)  # Time vector
f = 10  # Frequency of the sine wave

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Initial plots
line1, = ax[0].plot(t, np.sin(2 * np.pi * f * t), 'b-')
ax[0].set_title('Time Domain Signal')
ax[0].set_xlabel('Time')
ax[0].set_ylabel('Amplitude')
ax[0].set_ylim([-1.5, 1.5])
ax[0].grid(True)

frequencies = np.fft.fftfreq(t.shape[-1], d=1/fs)
line2, = ax[1].plot(frequencies, np.abs(np.fft.fft(np.sin(2 * np.pi * f * t))), 'b-')
ax[1].set_title('Magnitude of Fourier Transform')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('Magnitude')
ax[1].set_xlim([0, 50])
ax[1].set_ylim([0, 1200])
ax[1].grid(True)

def animate(damping_factor):
    y = np.exp(-damping_factor * t) * np.sin(2 * np.pi * f * t)
    line1.set_ydata(y)
    
    yf = np.abs(np.fft.fft(y))
    line2.set_ydata(yf)

ani = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 10, 100), repeat=False)

plt.tight_layout()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

NUMBER_OF_TERM = 20_000
DELTA = 500

def fourier_series_square_wave(x, terms):
  sum = 0
  for n in range(1, terms*2, 2):
    sum += (1/n) * np.sin(n * x)
  return (4/np.pi) * sum

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_original = np.sign(np.sin(x))

fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, y_original, label="Original Square Wave", linestyle="--", color="black")
approx_line, = ax.plot(x, fourier_series_square_wave(x, 1), label="Fourier Series Approximation")
ax.set_ylim(-2, 2)
ax.legend()
ax.grid(True)

def animate(i):
  y_approx = fourier_series_square_wave(x, i)
  approx_line.set_ydata(y_approx)
  approx_line.set_label(f"Fourier Series ({i} terms)")
  ax.legend()

ani = animation.FuncAnimation(fig, animate, frames=np.arange(1, NUMBER_OF_TERM, DELTA), repeat=False)

plt.title("Animated Fourier Series Approximation of a Square Wave")
plt.show()

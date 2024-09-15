import numpy as np
import matplotlib.pyplot as plt

def fourier_series_square_wave(x, terms):
    """Calculate the Fourier series approximation of a square wave."""
    sum = 0
    for n in range(1, terms*2, 2):  # Use odd numbers: 1, 3, 5, ...
        sum += (1/n) * np.sin(n * x)
    return (4/np.pi) * sum

x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_original = np.sign(np.sin(x))  # This is the ideal square wave

plt.figure(figsize=(10, 6))

# Plotting the original square wave
plt.plot(x, y_original, label="Original Square Wave", linestyle="--", color="black")

# Plotting the Fourier series approximations
for terms in [1, 2, 4, 500_000]:
    y_approx = fourier_series_square_wave(x, terms)
    plt.plot(x, y_approx, label=f"Fourier Series ({terms} terms)")

plt.ylim(-2, 2)
plt.title("Fourier Series Approximation of a Square Wave")
plt.legend()
plt.grid(True)
plt.show()

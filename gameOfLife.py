import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(frameNum, img, grid, N):
    # Copy grid since we require 8 neighbors for calculation
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            # Compute sum of eight neighbors
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)

            # Conway's rules
            if grid[i, j] == ON:  # If cell is currently alive
                if (total < 2) or (total > 3):
                    newGrid[i, j] = OFF
            else:  # If cell is currently dead
                if total == 3:
                    newGrid[i, j] = ON

    # Update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img

# Main function
if __name__ == '__main__':
    # Define grid size and animation update interval
    N = 100
    ON = 255  # Alive
    OFF = 0  # Dead
    UPDATE_INTERVAL = 50
    INITAL_FRAME = np.random.choice([ON, OFF], N*N, p=[0.2, 0.8]).reshape(N, N)

    fig, ax = plt.subplots()
    img = ax.imshow(INITAL_FRAME, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, INITAL_FRAME, N),
                                  frames=10, save_count=50, interval=UPDATE_INTERVAL)

    plt.show()

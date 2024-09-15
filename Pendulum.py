import numpy as np

# Physical constants
g = 9.81  # gravity (m/s^2)
l = 1.0  # long of pendulum (m)
m = 1.0  # mass (kg)
mu = 0.1  # air friction coefficient (kg/s)

# Initial conditions
theta_0 = np.pi/2  # initial angle (rad)
theta_dot_0 = 0.0  # initial angular velocity (rad/s)
delta_time = 0.01  # time step (s)

#defining the ODE
def get_theta_double_dot(theta, theta_dot):
  # The ODE describing the pendulum
  # theta_double_dot = -mu*theta_dot - (g/l)*np.sin(theta)
  # The first term is the air friction
  # The second term is the gravity
  return -mu*theta_dot - (g/l)*np.sin(theta)


# Solution to the ODE
def theta(final_time):
  # Initial conditions
  theta = theta_0
  theta_dot = theta_dot_0
  for time in np.arange(0, final_time, delta_time):
    theta_double_dot = get_theta_double_dot(theta, theta_dot)
    theta += theta_dot*delta_time
    theta_dot += theta_double_dot*delta_time
  return theta

# Print the solution
print(theta(10.0))

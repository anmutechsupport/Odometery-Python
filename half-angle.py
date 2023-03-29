import matplotlib.pyplot as plt
import numpy as np

# Define the starting position and heading of the robot
x0 = 0
y0 = 0
theta0 = np.pi / 4

# Define the change in heading angle
d_theta = np.pi / 2

# Compute the displacement vector using the half-angle approximation
delta_theta = d_theta / 2
delta_x = np.cos(theta0 + delta_theta) - np.cos(theta0)
delta_y = np.sin(theta0 + delta_theta) - np.sin(theta0)

# Compute the final position and heading of the robot
x1 = x0 + delta_x
y1 = y0 + delta_y
theta1 = theta0 + d_theta

# Plot the starting and final positions of the robot, as well as the displacement vector
fig, ax = plt.subplots()
ax.plot([x0, x1], [y0, y1], 'bo-', label='Displacement vector')
ax.plot(x0, y0, 'ro', label='Starting position')
ax.plot(x1, y1, 'go', label='Final position')
ax.legend()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.show()

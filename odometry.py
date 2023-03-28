import numpy as np
import matplotlib.pyplot as plt

# Parameters
R = 1  # radius of the wheels
L = 2  # distance between the wheels

# Initial state of the robot
x = 0
y = 0
theta = np.pi/4

# Target location
xt = 5
yt = 5

# Control inputs (angular velocities of the wheels)
w_l = 1  # rad/s
w_r = 2  # rad/s

# Time parameters
t0 = 0
tf = 10
dt = 0.1

# Lists to store robot pose and path
robot_poses = [(x,y)]
path = [(x,y)]

# Differential drive kinematics
def differential_drive(x, y, theta, w_l, w_r):
    v = R*(w_l + w_r)/2
    w = R*(w_r - w_l)/L
    x += v*np.cos(theta)*dt
    y += v*np.sin(theta)*dt
    theta += w*dt
    return x, y, theta

# Inverse kinematics
def inverse_kinematics(x, y, theta, xt, yt):
    dx = xt - x
    dy = yt - y
    rho = np.sqrt(dx**2 + dy**2)
    alpha = -theta + np.arctan2(dy, dx)
    beta = -theta - alpha
    w_l = (rho - L/2*alpha)/R
    w_r = (rho + L/2*alpha)/R
    return w_l, w_r

# Simulation loop
t = t0
while t < tf:
    w_l, w_r = inverse_kinematics(x, y, theta, xt, yt)
    x, y, theta = differential_drive(x, y, theta, w_l, w_r)
    t += dt
    robot_poses.append((x, y))
    path.append((xt, yt))

# Convert to numpy arrays for plotting
robot_poses = np.array(robot_poses)
path = np.array(path)

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(robot_poses[:, 0], robot_poses[:, 1], label='Robot path')
plt.plot(path[:, 0], path[:, 1], 'rx', label='Target')
plt.plot(0, 0, 'bo', label='Initial position')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.legend()
plt.show()

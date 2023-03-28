import math

class Robot:
    def __init__(self, x=0, y=0, theta=0, wheelbase=1, ticks_per_rev=1000):
        self.x = x
        self.y = y
        self.theta = theta
        self.wheelbase = wheelbase
        self.ticks_per_rev = ticks_per_rev
        self.left_ticks = 0
        self.right_ticks = 0
        self.last_left_ticks = 0
        self.last_right_ticks = 0
        self.distance_per_tick = (2 * math.pi * self.wheelbase) / self.ticks_per_rev

    def set_left_ticks(self, ticks):
        self.last_left_ticks = self.left_ticks
        self.left_ticks = ticks

    def set_right_ticks(self, ticks):
        self.last_right_ticks = self.right_ticks
        self.right_ticks = ticks

    def update_pose(self):
        delta_left_ticks = self.left_ticks - self.last_left_ticks
        delta_right_ticks = self.right_ticks - self.last_right_ticks
        delta_left_distance = delta_left_ticks * self.distance_per_tick
        delta_right_distance = delta_right_ticks * self.distance_per_tick
        delta_distance = (delta_left_distance + delta_right_distance) / 2
        delta_theta = (delta_right_distance - delta_left_distance) / self.wheelbase
        self.x += delta_distance * math.cos(self.theta + (delta_theta / 2))
        self.y += delta_distance * math.sin(self.theta + (delta_theta / 2))
        self.theta += delta_theta

if __name__ == '__main__':
    import time
    import random
    import matplotlib.pyplot as plt

    robot = Robot()
    x_data = [robot.x]
    y_data = [robot.y]

    for i in range(1000):
        robot.set_left_ticks(random.randint(0, 1000))
        robot.set_right_ticks(random.randint(0, 1000))
        robot.update_pose()
        x_data.append(robot.x)
        y_data.append(robot.y)

    plt.plot(x_data, y_data)
    plt.show()

import numpy as np
import matplotlib.pyplot as plt
g = 9.8  # acceleration due to gravity (m/s^2)
e = 0.8  # coefficient of restitution (bounciness)
dt = 0.01  # time step for simulation (s)
height = 10.0  # initial height (m)
velocity = 0.0  # initial velocity (m/s)
time = 0.0  # initial time (s)
heights = []
times = []

while height > 0:
    # Update velocity and height
    velocity -= g * dt
    height += velocity * dt

    if height <= 0:
        height = 0
        velocity = -e * velocity  # reverse velocity with coefficient of restitution
    
    time += dt
    heights.append(height)
    times.append(time)
    
plt.figure(figsize=(10, 5))
plt.plot(times, heights)
plt.title('Bouncing Ball Simulation')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.grid(True)
plt.show()

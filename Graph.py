import matplotlib.pyplot as plt
import numpy as np

# Parameters
g = 9.81  # gravitational acceleration (m/s^2)
h0 = 2.0  # initial height (m)
e = 0.75  # coefficient of restitution
num_bounces = 7  # number of bounces to simulate

# Time and height arrays
time = [0]
height = [h0]

# Simulate each bounce
t_total = 0
for i in range(num_bounces):
    # Time to fall and rise
    t_fall = np.sqrt(2 * h0 / g)
    t_rise = e * t_fall

    # Add times and heights for the fall and rise
    t_total += t_fall
    time.append(t_total)
    height.append(0)

    t_total += t_rise
    time.append(t_total)
    height.append(h0 * e**2)

    # Update height for next bounce
    h0 *= e**2

# Plot
plt.figure(figsize=(8, 5))
plt.plot(time, height, drawstyle='steps-post', marker='o')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.title('Bouncing Ball Under Gravity with Restitution (e=0.75)')
plt.grid(True)
plt.tight_layout()
plt.show()
from numpy import linspace
import matplotlib.pyplot as plt
# From Supratik Mukhopadhyay's slides

v0 = 5                         # Initial velocity (m/s)
g = 9.81                       # Acceleration of gravity (m/s^2)
t = linspace(0, 1, 1000)       # 1000 points in time interval
y = v0 * t - 0.5 * g * t**2    # Generate all heights

max_height = max(y)
print ("The maximum height achieved was %.3f m" % (max_height))

# We might also like to plot the path again just to compare
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

import sys
import configparser

from numpy import linspace
import matplotlib.pyplot as plt

print(len(sys.argv))
print(sys.argv)

celestial_body = sys.argv[1]
config = configparser.ConfigParser()
config.read("input.ini")

v0 = float(config.get(celestial_body, 'initial_speed'))     # Initial velocity
g  = float(config.get(celestial_body, 'surface_gravity'))   # Acceleration of gravity
t  = linspace(0, 1, 1000)                                   # 1000 points in time interval
y  = v0 * t - 0.5 * g * t**2                                # Generate all heights

max_height = max(y)
print ("The maximum height achieved was %f m" % (max_height))

# We might also like to plot the path again just to compare
plt.plot(t,y)
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.show()

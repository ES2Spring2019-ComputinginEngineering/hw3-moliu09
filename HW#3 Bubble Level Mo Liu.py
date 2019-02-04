#Name: Mo Liu
#Partner: Bo Eaves
#I worked on this assignmeng with Bo with assistance from Olivia.

import microbit
import math #importing the libraries

def measuring_tilt_in_3D(a, b, c):
    return math.atan2(a, math.sqrt(b**2+c**2))

while True:
    microbit.sleep(100)
    (x, y, z) = microbit.accelerometer.get_values() #this function doesn't take any parameter
    Ax = measuring_tilt_in_3D(x, y, z)
    Ay = measuring_tilt_in_3D(y, x, z)
    print("x = ",math.degrees(Ax))
    print("y = ",math.degrees(Ay))
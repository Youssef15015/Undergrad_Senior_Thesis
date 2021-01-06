import numpy as np
from math import pi

input_for_density= input('enter number:')
r= input('enter radius:')


volume = (pi*(float(r)**2))


density = float(input_for_density)/float(volume)


scaling = 0.29 *(density)**0.24


print(scaling)

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA


Y = np.array(np.genfromtxt('/home/yhe3/Documents/shifts.txt'))
Y = Y[1:len(Y)]
Z=[]

for i in Y:
	Z.append(LA.norm(i))

A = enumerate(Z)

plt.plot(np.array(Z))
plt.title('Movement of halo from timestep 24 to 504')
plt.xlabel('kpc')
plt.show()

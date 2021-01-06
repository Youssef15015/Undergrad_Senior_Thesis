import pynbody as pb
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA




s512= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512')
s012= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00012/h277.cosmo50cmb.3072g14HMbwK.00012')
s024= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024')
s036= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036')
s048= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00048/h277.cosmo50cmb.3072g14HMbwK.00048')
s060= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060')
s072= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072')
s084= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084')
s096= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00096/h277.cosmo50cmb.3072g14HMbwK.00096')
s108= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00108/h277.cosmo50cmb.3072g14HMbwK.00108')

sims= [s036,s048,s060,s072,s084,s096,s108]

#timesteps = np.arange(120,504,12)
#for timestep in timesteps: 
#	sims.append(pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+str(timestep)+'/h277.cosmo50cmb.3072g14HMbwK.00' + str(timestep)))


h512=s512.halos()[1]
print(h512)
X512 = np.array(h512['vel'])
print(X512)
X_norm512=[]
for i in X512:
	X_norm512.append(LA.norm(i))
print(X_norm512)
print(X_norm512.index(np.min(X_norm512)))
print(h512[X_norm512.index(np.min(X_norm512))])
position512= h512[X_norm512.index(np.min(X_norm512))]['pos']*50000
print(position512)

print(sims)



positions=[]
for s in sims:
	print (s)
	z=pb.analysis.cosmology.redshift(s,s.properties['time'].in_units('Gyr'))
	a = 1/(1+z)
	h1=s.halos()[1]
	X = np.array(h1['vel'])
	X_norm=[]
	for i in X:
		X_norm.append(LA.norm(i))
	positions.append(h1[X_norm.index(np.min(X_norm))]['pos']*50000/a)
	print(positions)

print(positions)	

vector_shifts= positions-position512
print(vector_shifts)

shifts=[]

for i in vector_shifts:
	shifts.append(enumerate(LA.norm(i)))

print(shifts)
plt.plot(shifts)

plt.show()

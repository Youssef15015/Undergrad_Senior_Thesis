#Calculate potential and total kinetic energy of a galaxy 

import pynbody as pb
import matplotlib.pyplot as plt
import numpy as np
import gc
from numpy.linalg import norm


s512= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512'
s012= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00012/h277.cosmo50cmb.3072g14HMbwK.00012'
s024= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024'
s036= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036'
s048= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00048/h277.cosmo50cmb.3072g14HMbwK.00048'
s060= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060'
s072= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072'
s084= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084'
s096= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00096/h277.cosmo50cmb.3072g14HMbwK.00096'
s108= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00108/h277.cosmo50cmb.3072g14HMbwK.00108'

sims= [s012,s024,s036,s048,s060,s072,s084,s096,s108]

timesteps = np.arange(120,504,12)
for timestep in timesteps:
	sims.append('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+str(timestep)+'/h277.cosmo50cmb.3072g14HMbwK.00' + str(timestep))
sims.append(s512)

ke=[]
pe=[]
pe2=[]
speed=[]
for sim in sims:
	s=pb.load(sim)
	print(s)
	s.physical_units()
	h1=s.halos()[1]
	pb.analysis.halo.center(h1)
	pb.analysis.angmom.faceon(h1,cen=(0,0,0))
	p= pb.analysis.profile.Profile(h1,ndim=3)
	T= 0.5*np.array(p['v_circ'].in_units('m s**-1'))**2
	ke.append(T.mean())
	print(ke)
	PHI2= np.array(p['pot'].in_units('m**2 s**-2'))
	pe2.append(PHI2.mean()/2)
	print(pe2)
	del s
	del h1
	del p
	gc.collect()
zero = 2*ke+pe
np.savetxt('/home/yhe3/Desktop/kineticenergies.txt',ke)
np.savetxt('/home/yhe3/Desktop/potentialenergies.txt',pe2)


steps=np.linspace(0,512,len(sims))

plt.plot(steps,ke)
plt.plot(steps,pe)
plt.plot(steps,zero)

plt.show()


	



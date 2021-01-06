#Print pics of Dark matter, Stars, and Gas for a timestep.
import matplotlib.pyplot as plt
timestep=str(input('Enter last three digits of timestep number:'))
import pynbody as pb
import numpy as np
s = pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
h = s.halos(sorton=True)
h1=h[1]
pb.analysis.halo.center(h[1],mode='hyb')
pb.plot



s=pb.plot.image(h1.s,width=80)
plt.savefig('/home/yhe3/Documents/h277_pics/s'+str(timestep)+'s')
del s
pb.plot.image(h1.g,width=80)
s=plt.savefig('/home/yhe3/Documents/h277_pics/s'+str(timestep)+'g')
del s
s=pb.plot.image(h1.dm,width=80)
del s
plt.savefig('/home/yhe3/Documents/h277_pics/s'+str(timestep)+'dm')


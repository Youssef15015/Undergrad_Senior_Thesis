import pynbody as pb
import numpy as np 
import matplotlib.pyplot as plt


timestep=input('last 3 digits of timestep:')
nbins= int(input('number of bins='))


s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
s.physical_units()
h1=s.halos()[1]
print(h1)
pb.analysis.halo.center(h1)
X=np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')
gas_mask=np.isin(h1.s['iord'],X)
filter_50= pb.filt.Sphere("50 kpc",(0,0,0))
filter_80= pb.filt.Sphere("80 kpc",(0,0,0))
filter_300= pb.filt.Sphere("300 kpc",(0,0,0))
count = str(len(h1.s[gas_mask][filter_300])-len(h1.s[gas_mask][filter_50]))

outerstars= h1.s[gas_mask]['r']>= 50 




plt.hist(h1.s[gas_mask][outerstars]['feh'],bins=nbins,range=(-4,0.5))
plt.title('time step =00'+timestep +' for h277'+' for r > 50')
plt.xlabel('Fe/H')
plt.show()


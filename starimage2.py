import pynbody as pb
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.font_manager as font

timestep=input('last 3 digits of timestep:')
nbins= int(input('number of bins='))


s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
s.physical_units()
h1=s.halos()[1]
pb.analysis.halo.center(h1)
X=np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')
gas_mask=np.isin(h1.s['iord'],X)

filter_50= pb.filt.Sphere("50 kpc",(0,0,0))
filter_200= pb.filt.Sphere("200 kpc",(0,0,0))
filter_300= pb.filt.Sphere("50 kpc",(0,0,0))


count = str(len(h1.s[gas_mask]['r']))
countB= str(len(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['r']))

plt.hist(h1.s[gas_mask]['r'],bins=nbins,histtype='step')
plt.title('Distance of '+count+' h277 clusters from center of galaxy in main halo', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.xlabel('r in kpc',fontsize=14)
plt.show()


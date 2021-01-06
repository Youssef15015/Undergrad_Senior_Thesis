import pynbody as pb
import numpy as np 
import matplotlib.pyplot as plt


timestep=input('last 3 digits of timestep:')
nbins= int(input('number of bins='))


s= pb.load('/data/REPOSITORY/e11Gals/h986.cosmo50cmb.3072g14HBWK/h986.cosmo50cmb.3072g14HBWK.00'+timestep+'/h986.cosmo50cmb.3072g14HBWK.00'+timestep)
s.physical_units()
h1=s.halos()[1]
pb.analysis.halo.center(h1)
X=np.genfromtxt('/home/yhe3/Desktop/hpids.txt')
gas_mask=np.isin(h1.s['iord'],X)
filter_50= pb.filt.Sphere("50 kpc",(0,0,0))
filter_200= pb.filt.Sphere("200 kpc",(0,0,0))
filter_150= pb.filt.Sphere("150 kpc",(0,0,0))

Y=plt.hist(h1.s[gas_mask]['r'],bins=nbins)
plt.title('time step =00'+timestep +' for h986 galaxy',font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22')

plt.xlabel('r in kpc')
plt.show()

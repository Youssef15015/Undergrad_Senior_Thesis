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
Y= [24.1,39.1,30.6,112.5,59.0,56.1,406.2,309.7,114.1,54.1,61.3,51.5,293.1,136.6,135.0,36.2,29.7,312,28.7,362.5,160.7,69.8,23.1,60.3,33.3,22.8,60,58,20.9,39.1,29,90.6,53.1,69.1,95.8,51.2,84.4,60.6,24.1,
20.2,15.0,18.9,42.1,15.6,233.4,14.0,12.4,19.2,36.5,8.8,11.7,8.1,10.8,6.8,27.4,97.1,14.7,12.1,13.7,15.0,9.8,125.2,5.5,5.5,24.4,6.8,6.2,7.5,8.5,31.3,3.6,5.5,5.5,24.4,4.6,10.8,58.4,2.6,16.3,3.3,1.6,16.6,
2.6,10.8,4.2,4.6,10.1,13.0,8.8,19.6,7.2,46.9,18.6,3.9,4.2,12.7,4.2,12.1,2.3,13.7,3.6,5.9,13.7,2.0,7.5,12.7,2.0,9.8,9.1,16.6,6.8,14.7,45.6,7.2,10.4,3.3,12.1,11.1,10.1,5.5,9.8,22.8,3.9,8.8,7.2,5.5,
5.5,8.8,16.0,17.9,7.2,16.0,11.4,61.6,7.8,8.5,16.3,17.0,15.6,30.0,50.9,20.9,69.8,12.7,63.2,26.7,21.8,47.9,41.7,42.1,125.5,33.9,33.9,23.1,51.5,87.7,82.5]
Y=np.array(Y)
Y= Y[Y>50]
Y= Y[Y<200]
gas_mask=np.isin(h1.s['iord'],X)

filter_50= pb.filt.Sphere("50 kpc",(0,0,0))
filter_200= pb.filt.Sphere("200 kpc",(0,0,0))
filter_300= pb.filt.Sphere("50 kpc",(0,0,0))


count = str(len(h1.s[gas_mask]['r']))
countB= str(len(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['r']))

fig,ax1=plt.subplots()

ax1.hist(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['r'],bins=nbins,histtype='step',color='r',label='Simulated Star Particles('+countB+')')




ax1.set_title('Radial Distance from Galactic Center', fontsize=12)
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)
ax1.set_xlabel('r in kpc',fontsize=14)
ax2=ax1.twinx()
ax2.hist(Y,bins=nbins,histtype='step',color='b',label='Galactic Globular Clusters('+str(len(Y))+')')
ax1.legend( fancybox=True,loc='upper left')
ax2.legend( fancybox=True,loc='center right')





plt.show()


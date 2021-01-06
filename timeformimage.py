import pynbody as pb
import numpy as np 
import matplotlib.pyplot as plt
from pynbody.analysis import cosmology

timestep=input('last 3 digits of timestep:')
nbins= int(input('number of bins='))
choice= int(input('1,2,or 3:'))

s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
s.physical_units()
h1=s.halos()[1]
pb.analysis.halo.center(h1)
X=np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')


gas_mask=np.isin(h1.s['iord'],X)
gas_mask2=np.isin(s.s['iord'],X)


if choice ==1:

	Z= np.array(h1.s[gas_mask]['age'].in_units('Gyr'))


	plt.hist(Z,bins=nbins,histtype='step')
	plt.title(r'Age of h277 clusters in main halo',fontsize=14)
	plt.xlabel(r'$Gyr$',fontsize=14)
	plt.tick_params(axis='both', which='major', labelsize=12)
	plt.tick_params(axis='both', which='minor', labelsize=10)
	plt.show()




elif choice==2:

        Z= np.array(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['age'].in_units('Gyr'))
        print(len(Z[Z<10.5]))
        print(len(Z))
        plt.hist(Z,bins=nbins,histtype='step')
        plt.title(r'Age of h277 clusters [r > 50 kpc] in main halo',fontsize=14)
        plt.xlabel(r'$Gyr$',fontsize=14)
        plt.tick_params(axis='both', which='major', labelsize=12)
        plt.tick_params(axis='both', which='minor', labelsize=10)
        plt.show()



elif choice ==3:

        Z= np.array(h1.s[gas_mask]['age'].in_units('Gyr'))


        fig,ax1=plt.subplots()
        ax1.hist(Z,bins=nbins,histtype='step',color='r',label='all of them')
        ax1.set_xlabel('$Age(Gyr)$',fontsize=14)
        ax1.tick_params(axis='both', which='major', labelsize=12)
        ax1.tick_params(axis='both', which='minor', labelsize=10)
        ax2=ax1.twinx()
        Z2= np.array(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['age'].in_units('Gyr'))
        ax2.hist(Z2,bins=nbins,histtype='step',color='b',label='outside of 50 kpc')
        ax2.set_xlabel('$Age(Gyr)$',fontsize=14)
        ax2.set_ylim([0,45])
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')
        ax1.set_title('Age of h277 Star Particles in Main Halo')
        plt.show()




import pynbody as pb
import numpy as np 
import matplotlib.pyplot as plt


timestep=input('last 3 digits of timestep:')
nbins= int(input('number of bins='))
xmin = float(input('minimum range:'))
xmax = float(input('maximum range:'))
choice= int(input('1,2,or 3:'))

s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
s.physical_units()
h1=s.halos()[1]
pb.analysis.halo.center(h1)
X=np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')
A= [-0.72,-1.32,-1.26,-0.7,-1.27,-0.65,-1.7,-1.43,-1.42,-1.18,-1.60,-1.92,-2.15,-1.20,-1.14,-0.83,-1.63,-1.59,-1.41,-1.80,-2.17,-1.68,-2.23,-1.85,-2.10,-2.27,-1.53,-1.50,-1.69,-1.30,-1.98,-1.88,-1.98,-1.53,-1.91,-1.41,-1.90,-1.29,0.00,-1.59,-1.01,-1.62,-1.75,-1.16,-1.98,-1.76,-1.65,-0.74,-1.02,-1.50,-1.53,-1.47,-1.37,-1.28,-1.56,-1.02,-2.07,-1.18,-1.74,-1.26,-2.10,-1.99,-0.45,-2.31,-1.25,-1.77,-0.55,-0.4,-1.37,-0.64,-1.7,-0.69,-0.59,-1.41,-1.00,-0.99,-0.33,-0.75,-1.03,-0.7,-0.55,-1.28,-1.02,-2.02,-0.91,-2.15,-1.51,-0.23,-0.36,-0.46,-0.56,-1.50,-0.64,-0.46,-1.05,-0.65,-1.23,-1.00,-1.34,-1.79,-0.11,-0.63,-1.35,-1.40,-1.81,-1.80,-0.18,-1.08,-1.32,-0.75,-0.50,-0.76,-1.30,-0.33,-1.50,-0.44,-1.32,-0.95,-0.64,-1.26,-0.81,-1.70,-0.37,-1.62,-1.02,-1.49,-1.26,-1.10,-1.60,-1.54,-0.4,-1.98,-0.32,-0.10,-1.75,-1.94,-2.16,-0.40,-0.78,-1.29,-1.47,-1.42,-1.52,-2.37,-1.65,-2.27,-0.85,-1.88,-1.78]


gas_mask=np.isin(h1.s['iord'],X)
gas_mask2=np.isin(s.s['iord'],X)


if choice ==1:

	Z= np.array((h1.s['feh']))
	fig,ax1=plt.subplots()

	ax1.hist(Z,bins=nbins,range=(xmin,xmax),histtype='step',label='All Star Paticles',color='r')
	ax1.set_title(r'Metallicities of Star Particles and Galactic GCs',fontsize=14)
	ax1.set_xlabel(r'[Fe/H]',fontsize=14)
	ax1.tick_params(axis='both', which='major', labelsize=12)
	ax1.tick_params(axis='both', which='minor', labelsize=10)
	ax2=ax1.twinx()
	ax2.hist(A,label='Galactic Globular Clusters',histtype='step',color='b')
	ax1.legend(loc='upper left')
	ax2.legend(loc='upper right')
	plt.show()




elif choice==2:

	Z= np.array(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['feh'])
	print(len(Z[Z >= -2.22]))

	fig,ax1=plt.subplots()
	ax1.hist(Z,bins=nbins,range=(xmin,xmax),histtype='step',color='r',label='Simulated Star Particles')
	ax1.set_title(r'Simulated Star Particles [r > 50 kpc]',fontsize=14)
	ax1.tick_params(axis='both', which='major', labelsize=12)
	ax1.tick_params(axis='both', which='minor', labelsize=10)
	ax1.set_xlabel(r'[Fe/H]',fontsize=14)
	ax2=ax1.twinx()
	ax2.hist(A,label='Galactic Globular Clusters',histtype='step',color='b')
	ax1.legend(loc='upper left')
	ax2.legend(loc='upperright')
	plt.show()




elif choice ==3:

        Z= np.array(h1.s[gas_mask][h1.s[gas_mask]['r']>50]['metals']*2)/(0.018)

        logplot=[]
        for x in Z:
                if x ==0:
                        logplot.append(-4)
                else:logplot.append(np.log10(x))



        plt.hist(logplot,bins=nbins,range=(xmin,xmax))
        plt.title('Metallicity')
        plt.xlabel('Z/Z_sun')
        plt.show()





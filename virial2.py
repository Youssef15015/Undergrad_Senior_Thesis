#Calculate potential and total kinetic energy of a galaxy 

import pynbody as pb
import matplotlib.pyplot as plt
import numpy as np
import gc
from astropy import units as u
from pynbody.util import get_eps
from pynbody.gravity import calc
from numpy.linalg import norm


s512= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512'
##s012= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00012/h277.cosmo50cmb.3072g14HMbwK.00012'
s024= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024'
s036= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036'
s048= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00048/h277.cosmo50cmb.3072g14HMbwK.00048'
s060= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060'
s072= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072'
s084= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084'
s096= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00096/h277.cosmo50cmb.3072g14HMbwK.00096'
s108= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00108/h277.cosmo50cmb.3072g14HMbwK.00108'

sims= [s024,s036,s048,s060,s072,s084,s096,s108]



timesteps = np.arange(120,504,12)
for timestep in timesteps:
	sims.append('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+str(timestep)+'/h277.cosmo50cmb.3072g14HMbwK.00' + str(timestep))
sims.append(s512)

Masses={'s1':4.1979725e+09,'s2':2.4327397e+10,'s3':3.9878902e+10,'s4':1.2979822e+11,'s5':1.6633561e+11,'s6':1.7349725e+11,'s7':2.6914382e+11,'s8':3.4920959e+11,'s9':3.7962328e+11,'s10':3.7793559e+11,'s11':3.9206712e+11,'s12':4.1701094e+11,'s13':4.3432192e+11,'s14':4.5187668e+11,'s15':4.6699728e+11,'s16':4.7702465e+11,'s17':4.8795753e+11,'s18':4.9456710e+11,'s19':5.0095614e+11,'s20':5.1034928e+11,'s21':5.2043150e+11,'s22':5.2789176e+11,'s23':5.3608632e+11,'s24':5.4345341e+11,'s25':5.5019589e+11,'s26':5.5603836e+11,'s27':5.6230130e+11,'s28':5.6856982e+11,'s29':5.7490407e+11,'s30':5.8402053e+11,'s31':5.9217537e+11,'s32':5.9961370e+11,'s33':6.0746301e+11,'s34':6.1523696e+11,'s35':6.2772052e+11,'s36':6.3605480e+11,'s37':6.4348219e+11,'s38':6.4638897e+11,'s39':6.5960962e+11,'s40':6.7287260e+11,'s41':6.7872870e+11}

Radii={'s1':54.1644,'s2':97.0959,'s3':114.3288,'s4':169.1507,'s5':183.3699,'s6':185.5342,'s7':214.2329,'s8':232.9863,'s9':238.7945,'s10':237.6164,'s11':239.6301,'s12':243.6164,'s13':245.8767,'s14':247.9863,'s15':249.4794,'s16':249.9452,'s17':250.4521,'s18':250.1233,'s19':249.6712,'s20':249.6301,'s21':249.5890,'s22':249.0548,'s23':248.5342,'s24':247.8082,'s25':246.9178,'s26':245.8082,'s27':244.6986,'s28':243.5206,'s29':242.2877,'s30':241.3699,'s31':240.2466,'s32':238.9589,'s33':237.6575,'s34':236.2877,'s35':235.4383,'s36':234.0000,'s37':232.3972,'s38':228.4521,'s39':229.1781,'s40':228.0685,'s41':226.9726}


ke=[]
pe=[]
pe2=[]
speed=[]

def avgphi(h1,R):
	e=0.17328767
	upper=h1.dm['r']<(R+5*e)
	lower=h1.dm[upper]['r']>(R-5*e)
	avgphi= h1.dm[upper][lower]['phi'].mean()
	return avgphi

def constant(M,R):
	c= M*4.3016024368114054e-06/R
	return c


k=1
for sim in sims:
	s=pb.load(sim)
	print(s)
	s.physical_units()
	h1=s.halos()[1]
	pb.analysis.halo.center(h1.dm)
	T= 0.5*np.array(h1.dm['vel'].in_units('km s**-1'))**2
	ke.append(T.sum())
	print(ke)
	R= pb.analysis.halo.virial_radius(h1.dm,rho_def='critical') 
	c= constant(Masses['s'+str(k)],R)
	avg=avgphi(h1.dm,R)
	inf_phi=np.array(avg)+np.array(c)
	PHI2= np.array(h1.dm['phi'].in_units('km**2 s**-2'))-inf_phi
	pe2.append(PHI2.sum()/2)
	print(pe2)
	del avg
	del c
	del inf_phi
	del s
	del h1
	gc.collect()
	k=k+1
zero = 2*ke+pe
np.savetxt('/home/yhe3/Desktop/kineticenergies3.txt',ke)
np.savetxt('/home/yhe3/Desktop/potentialenergies3.txt',pe2)


steps=np.linspace(0,512,len(sims))

plt.plot(steps,ke)
plt.plot(steps,pe)
plt.plot(steps,zero)

plt.show()


	



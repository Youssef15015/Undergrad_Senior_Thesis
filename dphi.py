# calculate the spatial deriviatives of phi

import pynbody as pb
import matplotlib.pyplot as plt
import numpy as np
import gc
from numpy.linalg import norm
from pynbody.util import get_eps
from pynbody import gravity

s512= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512'
s012= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00012/h277.cosmo50cmb.3072g14HMbwK.00012'
s024= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024'
s036= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036'
s048= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00048/h277.cosmo50cmb.3072g14HMbwK.00048'
s060= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060'
s072= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072'
s084= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084'
s096= '/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00096/h277.cosmo50cmb.3072g14HMbwK.00096'

sims= [s012,s024,s036,s048,s060,s072,s084,s096]

timesteps = np.arange(108,512,12)
for timestep in timesteps:
        sims.append('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+str(timestep)+'/h277.cosmo50cmb.3072g14HMbwK.00' + str(timestep))


s=sims[len(sims)-1]
s=pb.load(s)
s.physical_units()
h=s.halos()
pb.analysis.halo.center(h[1])
c= 138853.4081
h1=h[1]
PHI= np.array(h1['phi'].in_units('km**2 s**-2'))+c
dpdr=[]
drdx=[]
drdy=[]
drdz=[]
dpdxdr=[]
dpdydr=[]
dpdzdr=[]
	
for i in range(len(h1['phi'])-2):
		dpdr.append((h1['phi'][i+1]-h1['phi'][i])/(h1['r'][i+1]-h1['r'][i]))
		drdx.append((h1['r'][i+1]-h1['r'][i])/(h1['pos'][i+1][0])-h1['pos'][i][0])
		drdy.append((h1['r'][i+1]-h1['r'][i])/(h1['pos'][i+1][1])-h1['pos'][i][1])
		drdz.append((h1['r'][i+1]-h1['r'][i])/(h1['pos'][i+1][2])-h1['pos'][i][2])
dpdx= dpdr*drdx
dpdy= dpdr*drdy
dpdz= dpdr*drdz
for i in range(len(h1['phi'])-2):
		dpdxdr.append((dpdx[i+1]-dpdx[i])/(h1['r'][i+1])-h1['r'][i])
		dpdydr.append((dpdy[i+1]-dpdy[i])/(h1['r'][i+1])-h1['r'][i])
		dpdzdr.append((dpdz[i+1]-dpdz[i])/(h1['r'][i+1])-h1['r'][i])


dp2dx2= dpdxdr*drdx[1:len(drdx)]
dp2dy2= dpdydr*drdy[1:len(drdy)]
dp2dz2= dpdzdr*drdz[1:len(drdz)]
dp2dxdy=dpdxdr*drdy[1:len(drdy)]
dp2dxdz=dpdxdr*drdz[1:len(drdz)]
dp2dydx=dpdydr*drdx[1:len(drdx)]
dp2dydz=dpdydr*drdz[1:len(drdz)]
dp2dzdx=dpdzdr*drdx[1:len(drdx)]
dp2dzdy=dpdzdr*drdy[1:len(drdy)]


r= h1['r'][0:len(dp2dx2)].view(np.ndarray)

plt.plot(r,dpdx2)




	



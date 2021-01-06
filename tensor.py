import pynbody as pb
import numpy as np
import matplotlib.pyplot as plt
import numdifftools as nd
import numpy.linalg as LA


timestep=input('last 3 digits of timestep:')


s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
s.physical_units()

ids=np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')
gas_mask=np.isin(h1.s['iord'],X)
pb.analysis.halo.center(s.s[gas_mask][0])
filter = pb.filt.Sphere("1 kpc",(0,0,0))
A=np.histogramdd((s.s[filter]['phi'],3),bins=3)
H=nd.Hessian(A)
eigen=LA.eig(H)
eigen.sum()

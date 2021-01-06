import pynbody as pb
import numpy as np
import matplotlib.pyplot as plt
timestep=input('last 3 digits of timestep:')

def SFR(halo):
    weights = halo.st['massform'] # mass of each star particle at formation
    print (weights)
    tmax_yr = s.properties['time'].in_units('yr') # the timestep's time since the start of the simulation
    time_bin = 1000000000*(1/2)
    nbins = int(tmax_yr/time_bin) # number of time bins

    M,_ = np.histogram(halo.st['tform'].in_units("yr"),bins=nbins,weights=weights.in_units("Msol"),range=(0,tmax_yr)) #Total mass (in solar masses) of star particles in each bin of time defined in nbins
    SFR = M/np.diff(_)

    return SFR #Return star formation rate for the halo across all time bins up until the current time


s = pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
h = s.halos(sorton=True)
pb.analysis.halo.center(h[1],mode='hyb')
h1 = h[1][pb.filt.Sphere("20 kpc",(0,0,0))]

sfr = SFR(h[1])
print('sfr values')
print(sfr)
print('sum')
print(sfr.sum())
print('mean')
print(np.mean(sfr))



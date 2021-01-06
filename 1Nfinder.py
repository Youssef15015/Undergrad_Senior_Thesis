## print Number of clusters based in the region where 95 percent of the star formation occurs

import pynbody as pb
import numpy as np
import scipy.integrate as integrate
from math import pi


timestep= input('last three digits of timestep: ')
timestep2=input('last digits of previous timestep:')
lower_bound= 10000
upper_bound=1000000000
totalm=integrate.quad(lambda m: m**-1*np.exp(-m/(2*(10**5))),lower_bound,upper_bound)[0]
s = pb.load( /edit/ simulation name /edit/)
s2 = pb.load(/edit/ simulation name /edit/)

h=s.halos()
h2=s2.halos()
dt=h[1].properties['time'].in_units('yr')-h2[1].properties['time'].in_units('yr')




def drange2(start, stop, step):
    numelements = int((stop-start)/float(step))
    for i in range(numelements+1):
            yield start + i*step


def SFR(halo):
        sfr=halo.st['massform'].in_units('Msol')/halo.properties['time'].in_units('yr')
        return sfr.sum()

def radius(halo):
        for x  in drange2(0,300,1):
                r= 25-x
                filter= pb.filt.Sphere(str(r)+" "+"kpc",(0,0,0))
                sfr=SFR(h1[filter])
                if float(sfr)/float(sfr_0) <= 0.95:
                        break
        r_0= float(r)+1
        for x  in drange2(0,1,0.1):
                r= float(r_0)-x
                filter= pb.filt.Sphere(str(r)+" "+"kpc",(0,0,0))
                sfr=SFR(h1[filter])
                if float(sfr)/float(sfr_0) <= 0.95:
                        break
        r_0=float(r)+0.1
        for x  in drange2(0,1,0.01):
                r=float(r_0)-x
                filter= pb.filt.Sphere(str(r)+" "+"kpc",(0,0,0))
                sfr=SFR(h1[filter])
                if float(sfr)/float(sfr_0) <= 0.95:
                        break
        r_0=float(r)+0.01
        for x  in drange2(0,1,0.001):
                r=float(r_0)-x
                filter= pb.filt.Sphere(str(r)+" "+"kpc",(0,0,0))
                sfr=SFR(h1[filter])
                if float(sfr)/float(sfr_0) <= 0.95:
                        break
        return r

def ratio_masscluster(halo):
        area = (pi*(float(r)**2))
        density = float(sfr_0)/float(area)
        scaling = 0.29 *(density)**0.24
        return float(scaling)

h1=h[1]
pb.analysis.halo.center(h1,mode='hyb')
sfr_0=SFR(h1) 
print('sfr_0')
print(sfr_0)
r=radius(h1)
print('r')
print(r)
ratio=ratio_masscluster(h1)
print('ratio')
print(ratio_masscluster(h1))
Mass= ratio*sfr_0*dt
print('Mass')
print(Mass)
print('totalm')
print(totalm)
A=float(Mass)/float(totalm)


number=integrate.quad(lambda m: A*m**-2*np.exp(-m/(2*(10**5))),lower_bound,upper_bound)[0]
print(number)

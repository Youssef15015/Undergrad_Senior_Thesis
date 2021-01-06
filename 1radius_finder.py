## Find the radius where 95 percent of the starformation has occurred

import pynbody as pb

timestep= input('last three digits of timestep:')
initial_radius= input('initial radius:')
def drange2(start, stop, step):
	numelements = int((stop-start)/float(step))
	for i in range(numelements+1):
		yield start + i*step

def SFR(halo):
	sfr=halo.st['massform'].in_units('Msol')/halo.properties['time'].in_units('yr')
	return sfr.sum()


s = pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
h=s.halos()
h1=h[1]
pb.analysis.halo.center(h1,mode='hyb')
sfr_0=SFR(h1)
print('sfr_0 ='+str(sfr_0))


### r was found to be 7.6 for timestep 60, sfr=  0.8864817301177706
### r was found to be 34.1 for timestep 72, sfr= 2.7139784978367127

for x  in drange2(0,300,1):
        r= float(initial_radius)-x
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

print('sfr_0 =' + str(sfr_0))
print ('ratio =' +str(float(sfr)/float(sfr_0)))
print('radius =' +str(r) )



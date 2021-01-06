import pynbody as pb
from pynbody.analysis.halo import _com
from pynbody.analysis.halo import config
import numpy as np
import matplotlib.pyplot as plt
#start = int(input('starting number:'))
#end = int(input('ending number:'))
#number=int(input('halo number:'))


s512= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512')
#s012= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00012/h277.cosmo50cmb.3072g14HMbwK.00012')
s024= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024')
s036= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036')
s048= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00048/h277.cosmo50cmb.3072g14HMbwK.00048')
s060= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060')
s072= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072')
#s084= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084')
#s096= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00096/h277.cosmo50cmb.3072g14HMbwK.00096')
#s108= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00108/h277.cosmo50cmb.3072g14HMbwK.00108')

sims= [s036,s048,s060,s072]

#timesteps = np.arange(start,end,12)
#for timestep in timesteps: 
#	sims.append(pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+str(timestep)+'/h277.cosmo50cmb.3072g14HMbwK.00' + str(timestep)))


h512=s512.halos()[1]
mass=np.asarray(h512['mass'],dtype='double')
pos= np.asarray(h512['pos'],dtype='double')
num_threads=config['number_of_threads']
r= (h512['r'].max()-h512['r'].min())/2
position512=_com.shrink_sphere_center(pos,mass,100,0.7,r,num_threads)*50000*1.0000000000000053
print(position512)

positions=[]
for s in sims:
	print (s)
	a=s.properties['a']
	h1=s.halos()[1]
	mass=np.asarray(h1['mass'],dtype='double')
	pos= np.asarray(h1['pos'],dtype='double')
	num_threads=config['number_of_threads']
	r= (h1['r'].max()-h1['r'].min())/2
	positions.append(_com.shrink_sphere_center(pos,mass,100,0.7,r,num_threads)*50000/a)
print(positions)
vector_shifts= np.array(positions-position512)
#print(vector_shifts)

#X=np.genfromtxt('/home/yhe3/Documents/shifts.txt')
#X=np.append(np.array(X),vector_shifts,axis=0)
#np.savetxt('/home/yhe3/Documents/shifts.txt',X,fmt='%20f')



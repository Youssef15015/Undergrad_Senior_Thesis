import pynbody as pb
import numpy as np 


s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512')
s.physical_units()
h=s.halos()
h1= h[1]
pb.analysis.halo.center(h1)

Pressure=(h[1].s['rhoform'].in_units('g cm**-3')* h[1].s['tempform'])/(1.72*1.66054*10**-24)
logPressure=[]

for x in Pressure:
	logPressure.append(np.log10(x))

Pressure2 = (s.s['rhoform'].in_units('g cm**-3')* s.s['tempform'])/(1.72*1.66054*10**-24)



logPressure2=[]

for x in Pressure2:
	if x != 0:
		logPressure2.append(np.log10(x))



Y = h1.s[np.array(logPressure) > 5.5]

print(' number of high pressure stars in main halo')
print (len(Y['r']))

Y_50 = Y[Y['r']>50]
ids= Y_50['iord']
np.savetxt('/home/yhe3/Documents/outer350.txt',ids,fmt='%20d')

print(' number of high pressure stars outside of r 50 in main halo')
print(len(Y_50['r']))

print ('number of all high pressure stars')


G = s.s[1:len(s.s['r'])]
print(len(G[np.array(logPressure2) > 5.5]))

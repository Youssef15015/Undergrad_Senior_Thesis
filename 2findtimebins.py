import numpy as np
import pynbody as pb
import matplotlib.pyplot as plt
from numpy import linalg as LA


s=pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512')
s.physical_units()
h=s.halos()
pb.analysis.halo.center(h[1]) 
Pressure= h[1].s['rhoform'].in_units('g cm**-3')* h[1].s['tempform']/(h[1].s['mu']*1.66054*10**-24)
P_mask= Pressure >= 10**5
Ids_gas= h[1].s['igasorder']



#timeformations of each star
time= h[1].s['timeform']



#For time step beginning with 643 Myr, a.k.a 24. 
first=np.logical_and(time >= .322,
                     time <= .543)
# 36
second=np.logical_and(time >= .543,
                      time <= .864)

#I will skip 48 for now, 60

third=np.logical_and(time >= .864,
                      time <= 1.506)

fourth=np.logical_and(time >= 1.506,
                      time <=  1.827)

fifth=np.logical_and(time >= 1.827,
                      time <= 2.148)

sixth=np.logical_and(time >= 2.148,
                      time <= 2.469)

seventh=np.logical_and(time >= 2.469,
                      time <= 2.790)

eigth=np.logical_and(time >= 2.790,
                      time <= 3.111)

ninth=np.logical_and(time >= 3.111,
                      time <= 3.432)

tenth=np.logical_and(time >= 3.432,
                      time <= 3.753)

eleven=np.logical_and(time >= 3.753,
                      time <= 4.074)

twelve=np.logical_and(time >= 4.074,
                      time <= 4.397)

thirteen=np.logical_and(time >= 4.397,
                      time <= 4.716)

fourteen=np.logical_and(time >= 4.716,
                      time <= 5.037)

fifteen=np.logical_and(time >= 5.037,
                      time <= 5.358)

sixteen=np.logical_and(time >= 5.358,
                      time <= 5.679)

seventeen=np.logical_and(time >= 5.679,
                      time <= 6.000)

eighteen=np.logical_and(time >= 6.000,
                      time <= 6.321)

nineteen=np.logical_and(time >= 6.321,
                      time <= 6.642)

twenty=np.logical_and(time >= 6.642,
                      time <= 6.963)

twentyone=np.logical_and(time >= 6.963,
                      time <= 7.284)

twentytwo=np.logical_and(time >= 7.284,
                      time <= 7.605)

twentythree=np.logical_and(time >= 7.605,
                      time <= 7.926)

twentyfour=np.logical_and(time >= 7.926,
                      time <= 8.247)

twentyfive=np.logical_and(time >= 8.247,
                      time <= 8.568)

twentysix=np.logical_and(time >= 8.568,
                      time <= 8.889)

twentyseven=np.logical_and(time >= 8.889,
                      time <= 9.210)

twentyeight=np.logical_and(time >= 9.210,
                      time <= 9.531)

twentynine=np.logical_and(time >= 9.531,
                      time <= 9.852)

thirty=np.logical_and(time >= 9.852,
                      time <= 10.173)

thirtyone=np.logical_and(time >= 10.173,
                      time <= 10.494)

thirtytwo=np.logical_and(time >= 10.494,
                      time <= 10.815)

thirtythree=np.logical_and(time >= 10.815,
                      time <= 11.136)

thirtyfour=np.logical_and(time >= 11.136,
                      time <= 11.457)

thirtyfive=np.logical_and(time >= 11.457,
                      time <= 11.778)

thirtysix=np.logical_and(time >= 11.778,
                      time <= 12.099)

thirtyseven=np.logical_and(time >= 12.099,
                      time <= 12.419)

thirtyeight=np.logical_and(time >= 12.419,
                      time <= 12.741)

thirtynine=np.logical_and(time >= 12.741,
                      time <= 13.062)

fourty=np.logical_and(time >= 13.062,
                      time <= 13.383)

fourtyone=np.logical_and(time >= 13.383,
                      time <= 13.583) 

fourtytwo=np.logical_and(time >= 13.583,
                      time <= 14)











print('-------------------------------------------------------------------')


table=[]

ids_gas = [Ids_gas[i] for i in range(len(Ids_gas)) if  first[i] and Pressure[i] >=10**5  ]
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
gas_mask1= np.isin(h1.s['igasorder'],ids_gas)
s1a=h1.s[gas_mask1]
j=(s1a['r'].in_units('kpc'))
j2=(s1a['pos'].in_units('kpc'))
j3=[]
for i in j2:
	j3.append(LA.norm(i))
for i in (j3-np.array(j)):
        table.append(i)


ids_gas = [Ids_gas[i] for i in range(len(Ids_gas)) if  second[i] and Pressure[i] >=10**5  ]
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
gas_mask1= np.isin(h1.s['igasorder'],ids_gas)
s1a=h1.s[gas_mask1]
j=(s1a['r'].in_units('kpc'))
j2=(s1a['pos'].in_units('kpc'))
j3=[]
for i in j2:
	j3.append(LA.norm(i))
for i in (j3-np.array(j)):
	table.append(i)


ids_gas = [Ids_gas[i] for i in range(len(Ids_gas)) if  third[i] and Pressure[i] >=10**5  ]
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
gas_mask1= np.isin(h1.s['igasorder'],ids_gas)
s1a=h1.s[gas_mask1]
j=(s1a['r'].in_units('kpc'))
j2=(s1a['pos'].in_units('kpc'))
j3=[]
for i in j2:
	j3.append(LA.norm(i))
for i in (j3-np.array(j)):
        table.append(i)




ids_gas = [Ids_gas[i] for i in range(len(Ids_gas)) if  fourth[i] and Pressure[i] >=10**5  ]
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
gas_mask1= np.isin(h1.s['igasorder'],ids_gas)
s1a=h1.s[gas_mask1]
j=(s1a['r'].in_units('kpc'))
j2=(s1a['pos'].in_units('kpc'))
j3=[]
for i in j2:
	j3.append(LA.norm(i))
for i in (j3-np.array(j)):
        table.append(i)


ids_gas = [Ids_gas[i] for i in range(len(Ids_gas)) if  fifth[i] and Pressure[i] >=10**5  ]
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
gas_mask1= np.isin(h1.s['igasorder'],ids_gas)
s1a=h1.s[gas_mask1]
j=(s1a['r'].in_units('kpc'))
j2=(s1a['pos'].in_units('kpc'))
j3=[]
for i in j2:
	j3.append(LA.norm(i))
for i in (j3-np.array(j)):
        table.append(i)

plt.hist(table)

plt.show()
















































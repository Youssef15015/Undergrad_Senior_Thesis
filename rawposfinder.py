import numpy as np
import pynbody as pb
import matplotlib.pyplot as plt
from numpy import linalg as LA


s=pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00512/h277.cosmo50cmb.3072g14HMbwK.00512')
s.physical_units()
h=s.halos()


ids= np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')



#timeformations of each star
time= h[1].s['tform'].in_units('Gyr')





first=np.logical_and(time >= .321,
                     time <= .642)
# 36
second=np.logical_and(time >= .642,
                      time <= .963)

#I will skip 48 for now, 60

third=np.logical_and(time >= .963,
                      time <= 1.284)

fourth=np.logical_and(time >= 1.284,
                      time <= 1.605)

fifth=np.logical_and(time >= 1.605,
                      time <=1.926 )

sixth=np.logical_and(time >= 1.926,
                      time <= 2.247)

seventh=np.logical_and(time >= 2.247,
                      time <= 2.568)

eigth=np.logical_and(time >= 2.568,
                      time <= 2.889)

ninth=np.logical_and(time >= 2.889,
                      time <= 3.21)

tenth=np.logical_and(time >= 3.21,
                      time <= 3.531)

eleven=np.logical_and(time >= 3.531,
                      time <= 3.852)

twelve=np.logical_and(time >= 3.852,
                      time <= 4.173)

thirteen=np.logical_and(time >= 4.173,
                      time <= 4.494)

fourteen=np.logical_and(time >= 4.494,
                      time <= 4.815)

fifteen=np.logical_and(time >= 4.815,
                      time <= 5.136)

sixteen=np.logical_and(time >= 5.136,
                      time <= 5.457)

seventeen=np.logical_and(time >= 5.457,
                      time <= 5.778)

eighteen=np.logical_and(time >= 5.778,
                      time <= 6.099)

nineteen=np.logical_and(time >= 6.099,
                      time <= 6.42)

twenty=np.logical_and(time >= 6.42,
                      time <= 6.741)

twentyone=np.logical_and(time >= 6.741,
                      time <= 7.062)

twentytwo=np.logical_and(time >= 7.062,
                      time <= 7.383)

twentythree=np.logical_and(time >= 7.383,
                      time <= 7.704)

twentyfour=np.logical_and(time >= 7.704,
                      time <= 8.025)

twentyfive=np.logical_and(time >= 8.025,
                      time <= 8.346)

twentysix=np.logical_and(time >= 8.346,
                      time <= 8.667)

twentyseven=np.logical_and(time >= 8.667,
                      time <= 8.988)

twentyeight=np.logical_and(time >= 8.988,
                      time <= 9.309)

twentynine=np.logical_and(time >= 9.309,
                      time <= 9.63)

thirty=np.logical_and(time >= 9.63,
                      time <= 9.951)

thirtyone=np.logical_and(time >= 9.951,
                      time <= 10.272)

thirtytwo=np.logical_and(time >= 10.272,
                      time <= 10.593)

thirtythree=np.logical_and(time >= 10.593,
                      time <= 10.914)

thirtyfour=np.logical_and(time >= 10.914,
                      time <= 11.235)

thirtyfive=np.logical_and(time >= 11.235,
                      time <= 11.556)

thirtysix=np.logical_and(time >= 11.556,
                      time <= 11.877)

thirtyseven=np.logical_and(time >= 11.877,
                      time <= 12.198)

thirtyeight=np.logical_and(time >= 12.198,
                      time <= 12.519)

thirtynine=np.logical_and(time >= 12.519,
                      time <= 12.84)

fourty=np.logical_and(time >= 12.84,
                      time <= 13.161)

fourtyone=np.logical_and(time >= 13.161,
                      time <= 13.482)

fourtytwo=np.logical_and(time >= 13.482,
                      time < 13.803)








print('-------------------------------------------------------------------')


table=[]

##First
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00024/h277.cosmo50cmb.3072g14HMbwK.00024')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

first=np.logical_and(time >= .321,
                     time <= .642)

stars= h1.s[first]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

##Second
s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00036/h277.cosmo50cmb.3072g14HMbwK.00036')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

second=np.logical_and(time >= .642,
                      time <= .963)


stars= h1.s[second]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]

j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))
##Third

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00060/h277.cosmo50cmb.3072g14HMbwK.00060')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

third=np.logical_and(time >= .963,
                      time <= 1.284)

stars= h1.s[third]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

##Fourth

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00072/h277.cosmo50cmb.3072g14HMbwK.00072')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

fourth=np.logical_and(time >= 1.284,
                      time <= 1.605)

stars= h1.s[fourth]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

##Fifth


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00084/h277.cosmo50cmb.3072g14HMbwK.00084')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

fifth=np.logical_and(time >= 1.605,
                      time <=1.926 )

stars= h1.s[fifth]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00096/h277.cosmo50cmb.3072g14HMbwK.00096')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

sixth=np.logical_and(time >= 1.926,
                      time <= 2.247)


stars= h1.s[sixth]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00108/h277.cosmo50cmb.3072g14HMbwK.00108')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

seventh=np.logical_and(time >= 2.247,
                      time <= 2.568)


stars= h1.s[seventh]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00120/h277.cosmo50cmb.3072g14HMbwK.00120')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

eigth=np.logical_and(time >= 2.568,
                      time <= 2.889)


stars= h1.s[eigth]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))



s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00132/h277.cosmo50cmb.3072g14HMbwK.00132')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')

ninth=np.logical_and(time >= 2.889,
                      time <= 3.21)

stars= h1.s[ninth]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00144/h277.cosmo50cmb.3072g14HMbwK.00144')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
tenth=np.logical_and(time >= 3.21,
                      time <= 3.531)


stars= h1.s[tenth]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00156/h277.cosmo50cmb.3072g14HMbwK.00156')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
eleven=np.logical_and(time >= 3.531,
                      time <= 3.852)

stars= h1.s[eleven]
pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]

j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00168/h277.cosmo50cmb.3072g14HMbwK.00168')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twelve=np.logical_and(time >= 3.852,
                      time <= 4.173)
stars= h1.s[twelve]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00180/h277.cosmo50cmb.3072g14HMbwK.00180')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirteen=np.logical_and(time >= 4.173,
                      time <= 4.494)
stars= h1.s[thirteen]



pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00192/h277.cosmo50cmb.3072g14HMbwK.00192')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
fourteen=np.logical_and(time >= 4.494,
                      time <= 4.815)
stars= h1.s[fourteen]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))



s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00204/h277.cosmo50cmb.3072g14HMbwK.00204')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
fifteen=np.logical_and(time >= 4.815,
                      time <= 5.136)
stars= h1.s[fifteen]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00216/h277.cosmo50cmb.3072g14HMbwK.00216')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
sixteen=np.logical_and(time >= 5.136,
                      time <= 5.457)
stars= h1.s[sixteen]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))




s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00228/h277.cosmo50cmb.3072g14HMbwK.00228')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
seventeen=np.logical_and(time >= 5.457,
                      time <= 5.778)
stars=h1.s[seventeen]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00240/h277.cosmo50cmb.3072g14HMbwK.00240')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
eighteen=np.logical_and(time >= 5.778,
                      time <= 6.099)
stars= h1.s[eighteen]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00252/h277.cosmo50cmb.3072g14HMbwK.00252')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)

time= h1.s['tform'].in_units('Gyr')
nineteen=np.logical_and(time >= 6.099,
                      time <= 6.42)
stars= h1.s[nineteen]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00264/h277.cosmo50cmb.3072g14HMbwK.00264')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twenty=np.logical_and(time >= 6.42,
                      time <= 6.741)
stars= h1.s[twenty]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00276/h277.cosmo50cmb.3072g14HMbwK.00276')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentyone=np.logical_and(time >= 6.741,
                      time <= 7.062)
stars= h1.s[twentyone]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00288/h277.cosmo50cmb.3072g14HMbwK.00288')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentytwo=np.logical_and(time >= 7.062,
                      time <= 7.383)
stars= h1.s[twentytwo]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00300/h277.cosmo50cmb.3072g14HMbwK.00300')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentythree=np.logical_and(time >= 7.383,
                      time <= 7.704)
stars= h1.s[twentythree]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00312/h277.cosmo50cmb.3072g14HMbwK.00312')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)

time= h1.s['tform'].in_units('Gyr')
twentyfour=np.logical_and(time >= 7.704,
                      time <= 8.025)
stars= h1.s[twentyfour]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00324/h277.cosmo50cmb.3072g14HMbwK.00324')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)

time= h1.s['tform'].in_units('Gyr')
twentyfive=np.logical_and(time >= 8.025,
                      time <= 8.346)
stars= h1.s[twentyfive]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00336/h277.cosmo50cmb.3072g14HMbwK.00336')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentysix=np.logical_and(time >= 8.346,
                      time <= 8.667)
stars= h1.s[twentysix]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00348/h277.cosmo50cmb.3072g14HMbwK.00348')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentyseven=np.logical_and(time >= 8.667,
                      time <= 8.988)
stars= h1.s[twentyseven]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00360/h277.cosmo50cmb.3072g14HMbwK.00360')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentyeight=np.logical_and(time >= 8.988,
                      time <= 9.309)
stars= h1.s[twentyeight]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00372/h277.cosmo50cmb.3072g14HMbwK.00372')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
twentynine=np.logical_and(time >= 9.309,
                      time <= 9.63)
stars= h1.s[twentynine]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00384/h277.cosmo50cmb.3072g14HMbwK.00384')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirty=np.logical_and(time >= 9.63,
                      time <= 9.951)
stars= h1.s[thirty]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00396/h277.cosmo50cmb.3072g14HMbwK.00396')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtyone=np.logical_and(time >= 9.951,
                      time <= 10.272)
stars= h1.s[thirtyone]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00408/h277.cosmo50cmb.3072g14HMbwK.00408')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtytwo=np.logical_and(time >= 10.272,
                      time <= 10.593)
stars= h1.s[thirtytwo]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00420/h277.cosmo50cmb.3072g14HMbwK.00420')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtythree=np.logical_and(time >= 10.593,
                      time <= 10.914)
stars= h1.s[thirtythree]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00432/h277.cosmo50cmb.3072g14HMbwK.00432')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtyfour=np.logical_and(time >= 10.914,
                      time <= 11.235)
stars= h1.s[thirtyfour]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)

s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00444/h277.cosmo50cmb.3072g14HMbwK.00444')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtyfive=np.logical_and(time >= 11.235,
                      time <= 11.556)
stars= h1.s[thirtyfive]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00456/h277.cosmo50cmb.3072g14HMbwK.00456')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtysix=np.logical_and(time >= 11.556,
                      time <= 11.877)
stars= h1.s[thirtysix]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00468/h277.cosmo50cmb.3072g14HMbwK.00468')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtyseven=np.logical_and(time >= 11.877,
                      time <= 12.198)
stars= h1.s[thirtyseven]


pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00480/h277.cosmo50cmb.3072g14HMbwK.00480')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtyeight=np.logical_and(time >= 12.198,
                      time <= 12.519)
stars= h1.s[thirtyeight]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00492/h277.cosmo50cmb.3072g14HMbwK.00492')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
thirtynine=np.logical_and(time >= 12.519,
                      time <= 12.84)
stars= h1.s[thirtynine]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

print(table)


s1= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00504/h277.cosmo50cmb.3072g14HMbwK.00504')
s.physical_units()
h1=s1.halos()[1]
pb.analysis.halo.center(h1)
time= h1.s['tform'].in_units('Gyr')
fourty=np.logical_and(time >= 12.84,
                      time <= 13.161)
stars= h1.s[fourty]

pressure= stars['rhoform'].in_units('g cm**-3')*stars['tempform']/(1.72*1.66054e-24)
s1a=stars[pressure >10**5.5]
j=np.array((s1a['posform']))
for i in j:
	table.append(LA.norm(i))

table=table*50000


np.savetxt('/home/yhe3/Desktop/dr.txt',table)




plt.hist(table)
plt.show()






















































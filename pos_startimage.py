import pynbody as pb
import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as LA


timestep=input('last 3 digits of timestep:')
nbins= int(input('number of bins='))
choice= int(input('1,2,or 3:'))

ids_305= np.genfromtxt('/home/yhe3/Documents/outer350.txt')





##simulation



s= pb.load('/data/REPOSITORY/e12Gals/h277.cosmo50cmb.3072g14HMbwK/h277.cosmo50cmb.3072g14HMbwK.00'+timestep+'/h277.cosmo50cmb.3072g14HMbwK.00'+timestep)
h1=s.halos()[1]
Pressure=(h1.s['rhoform'].in_units('g cm**-3')* h1.s['tempform'])/(1.72*1.66054*10**-24)





time = h1.s[Pressure > 10**5.5]['timeform'].in_units('Gyr')
time2= h1.s[np.isin(h1.s['iord'],ids_305)]['timeform'].in_units('Gyr')
print(time2)








### time domains






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



#### outer halo time ranges

ofirst=np.logical_and(time2 >= .321,
                     time2 <= .642)
# 36
osecond=np.logical_and(time2 >= .642,
                      time2 <= .963)

#I will skip 48 for now, 60

othird=np.logical_and(time2 >= .963,
                      time2 <= 1.284)

ofourth=np.logical_and(time2 >= 1.284,
                      time2 <= 1.605)

ofifth=np.logical_and(time2 >= 1.605,
                      time2 <=1.926 )

osixth=np.logical_and(time2 >= 1.926,
                      time2 <= 2.247)

oseventh=np.logical_and(time2 >= 2.247,
                      time2 <= 2.568)

oeigth=np.logical_and(time2 >= 2.568,
                      time2 <= 2.889)

oninth=np.logical_and(time2 >= 2.889,
                      time2 <= 3.21)

otenth=np.logical_and(time2 >= 3.21,
                      time2 <= 3.531)

oeleven=np.logical_and(time2 >= 3.531,
                      time2 <= 3.852)

otwelve=np.logical_and(time2 >= 3.852,
                      time2 <= 4.173)

othirteen=np.logical_and(time2 >= 4.173,
                      time2 <= 4.494)

ofourteen=np.logical_and(time2 >= 4.494,
                      time2 <= 4.815)



















X=np.genfromtxt('/home/yhe3/Documents/hpid_5.5_277_all.txt')
Y=np.array(np.genfromtxt('/home/yhe3/Documents/halopos.txt'))


gas_mask=np.isin(h1.s['iord'],X)
gas_mask2=np.isin(s.s['iord'],X)



if choice ==1:
	Z = []
	times = h1.s[Pressure > 10**5.5]['timeform'].in_units('Gyr')
	times2 = times[0:np.size(times)-15]
	zform=pb.analysis.cosmology.redshift(s,np.array(times2))
	zform=np.append(zform,np.zeros(15))
	aform = 1/(1+zform)	
	posform= h1.s[Pressure > 10**5.5]['posform']*(5*10**4)
	posform= np.array(posform)
	for i in range(len(posform)):
		for j in range(len(posform[i])):
			posform[i][j]=posform[i][j]*aform[i]


	posform[first] -= Y[1]
	posform[second] -= Y[2]
	posform[third] -= Y[3]
	posform[fourth] -= Y[4]
	posform[fifth] -= Y[5]
	posform[sixth] -= Y[6]
	posform[seventh] -= Y[7]
	posform[eigth] -= Y[8]
	posform[ninth] -= Y[9]
	posform[tenth] -= Y[10]
	posform[eleven] -= Y[11]
	posform[twelve] -= Y[12]
	posform[thirteen] -= Y[13]
	posform[fourteen] -= Y[14]
	posform[fifteen] -= Y[15]
	posform[sixteen] -= Y[16]
	posform[seventeen] -= Y[17]
	posform[eighteen] -= Y[18]
	posform[nineteen] -= Y[19]
	posform[twenty] -= Y[20]
	posform[twentyone] -= Y[21]
	posform[twentytwo] -= Y[22]
	posform[twentythree] -= Y[23]
	posform[twentyfour] -= Y[24]
	posform[twentyfive] -= Y[25]
	posform[twentysix] -= Y[26]
	posform[twentyseven] -= Y[27]
	posform[twentyeight] -= Y[28]
	posform[twentynine] -= Y[29]
	posform[thirty] -= Y[30]
	posform[thirtyone] -= Y[31]
	posform[thirtytwo] -= Y[32]
	posform[thirtythree] -= Y[33]
	posform[thirtyfour] -= Y[34]
	posform[thirtyfive] -= Y[35]
	posform[thirtysix] -= Y[36]
	posform[thirtyseven] -= Y[37]
	posform[thirtyeight] -= Y[38]
	posform[thirtynine] -= Y[39]
	posform[fourty] -= Y[40]
	posform[fourtyone] -= Y[41]
	posform[fourtytwo] -= Y[42]


	for i in posform:
		Z.append(LA.norm(i))
	Z= np.array(Z)
	np.savetxt('/home/yhe3/Desktop/d_form.txt',Z)
	fig,ax1=plt.subplots()
	ax1.hist(Z,bins=nbins,histtype='step')
	ax1.set_title(r'Distance of Clusters from Center of Galaxy When They Formed',fontsize=12)
	ax1.tick_params(axis='both', which='major', labelsize=12)
	ax1.tick_params(axis='both', which='minor', labelsize=10)
	ax1.set_xlabel(r'$kpc$',fontsize=14)







	A = []
	times = h1.s[np.isin(h1.s['iord'],ids_305)]['timeform'].in_units('Gyr')
	zform=pb.analysis.cosmology.redshift(s,np.array(times))
	aform = 1/(1+zform)
	posform= h1.s[np.isin(h1.s['iord'],ids_305)]['posform']*(5*10**4)
	posform= np.array(posform)
	for i in range(len(posform)):
		for j in range(len(posform[i])):
			posform[i][j]=posform[i][j]*aform[i]

	
	posform[ofirst]-= Y[1]
	posform[osecond]-= Y[2]
	posform[othird] -= Y[3]
	posform[ofourth]-= Y[4]
	posform[ofifth]-=Y[5]
	posform[osixth] -= Y[6]
	posform[oseventh] -= Y[7]
	posform[oeigth] -= Y[8]
	posform[oninth] -= Y[9]
	posform[otenth] -= Y[10]
	posform[oeleven] -= Y[11]
	posform[otwelve] -= Y[12]
	posform[othirteen] -= Y[13]
	posform[ofourteen] -= Y[14]
	

	for i in posform:
		A.append(LA.norm(i))
	A= np.array(A)
	np.savetxt('/home/yhe3/Desktop/outer_form.txt',A)



	ax2=ax1.twinx()
	ax2.hist(A,bins=nbins,histtype='step')
	fig.legend(loc='best')
	plt.tick_params(axis='both', which='major', labelsize=12)
	plt.tick_params(axis='both', which='minor', labelsize=10)
	plt.show()








Z = [-0.72,-1.32,-1.26,-0.7,-1.27,-0.65,-1.7,-1.43,-1.18,-1.60,-1.92,-2.15,-1.20,-1.14,-0.83,-1.63,-1.59,-1.41,-1.80,-2.17,-1.68,-2.23,-1.85,-2.10,-2.27,-1.53,-1.50,-1.69,-1.30,-1.98,-1.88,-1.98,-1.53,-1.91,-1.41,-1.90,-1.29,-0.49,-1.29,0.00,-1.59,-1.01,-1.62,-1.75,-1.16,-1.98,-1.76,-1.65,-0.74,-1.02,-1.50,-1.53,-1.47,-1.37,-1.28,-1.56,-1.02,-2.07,-1.18,-1.74,-1.26,-2.10,-1.99,-0.45,-0.45,-2.31,-1.25,-1.77,-0.55,-0.4,-1.37,-0.64,-1.70,-0.69,-0.59,-1.41,-1.00,-0.99,-0.33,-0.75,-1.03,-0.70,-0.55,-1.28,-1.02,-2.02,-0.91,-2.15,-1.51,-0.23,-0.36,-0.46,-0.56,-1.50,-0.64,-0.46,-1.05,-0.65,-1.23,-1.00,-1.34,-1.79,-0.11,-0.63,-1.35,-1.40,-1.81,-1.80,-0.18,-1.08,-1.32,-0.75,-0.5,-0.76,-1.30,-0.33,-1.50,-0.44,-1.32,-0.95,-0.64,-1.26,-0.81,-1.70,-0.37,-1.62,-1.02,-1.49,-1.26,-1.10,-1.60,-1.54,-0.40,-1.98,-0.32,-0.10,-1.75,-1.94,-2.16,-0.40,-0.78,-1.29,-1.47,-1.42,-1.52,-2.37,-1.65,-2.27,-0.85,-1.88,-1.78]



import numpy as np
import matplotlib.pyplot as plt
Z = np.array(Z)



plt.hist(Z,bins=30,histtype='step')
plt.title('Metallicities of '+str(len(Z))+' globular clusters',fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.xlabel('kpc',fontsize=14)
plt.show()



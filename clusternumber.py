import numpy as np
import scipy
from scipy import integrate as intg
import scipy.special as special

mass= float(input('lower bound of mass:'))
Mc=2*(10**5)

ans=intg.quad(lambda x: (x**-2) ,mass,10**11)

print(ans)


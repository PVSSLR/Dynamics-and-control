#TO SIMULATE HIV INFECTION USING ODE

import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint

#ODE MODEL FUNCTION

def model(x,t):
    H = x[0]
    I = x[1]
    V = x[2]
    
    dhdt = kr1 - kr2 * H - kr3 * H * V
    didt = kr3 * H * V - kr4 * I
    dvdt = - kr3 * H * V - kr5 * V + kr6 * I 
    
    dzdt = [dhdt,didt,dvdt]
    return dzdt 

#INITIAL CONDITIONS 
x =  [1000000,0, 100]        # Virus population 
kr1 = 1e5       # new healthy cells per year
kr2 = 0.1         # death rate of healthy cells
kr3 = 2e-7       # healthy cells converting to infected cells
kr4 = 0.5         # death rate of infected cells
kr5 = 5           # death rate of virus
kr6 = 100         # production of virus by infected cells

t = np.linspace(0,15,1000)

z = odeint(model,x,t)
#Plot
plt.semilogy(t,z[:,0],'b',label = 'H')
plt.semilogy(t,z[:,1],'g:',label = 'I')
plt.semilogy(t,z[:,2],'r--',label = 'V')
plt.xlabel('years')
plt.ylabel('States log scale')
plt.legend()
plt.show()


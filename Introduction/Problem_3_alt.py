import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

def fun_diff(z,t):
    dxdt = 3 * np.exp(-t)
    dydt = 3 - z[1]
    dzdt = [dxdt,dydt]
    return dzdt

#Initial Conditions 
z0 = [0,0]
t = np.linspace(0,30)
print(t)
print(z0)
#ODE
 
z = odeint(fun_diff,z0,t)
print(z)
#plot 
plt.plot(t,z[:,0],'r-')
plt.plot(t,z[:,1],'b-')
plt.show()
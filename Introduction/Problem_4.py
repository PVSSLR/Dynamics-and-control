#Problem 4  
#http://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations

import numpy as np 
from scipy.integrate import odeint 
import matplotlib.pyplot as plt 

def model(z,t):
    if (t > 5):
        u = 2
    else:
        u = 0    
    x = z[0]
    y = z[1]
    dxdt = (- x + u ) / 2
    dydt = (- y + x) / 5
    dzdt = [dxdt,dydt]
    return dzdt

#initial conditions 
z0=[0,0]
t = np.linspace(0,40,201)

#Solve ode 
z = odeint(model,z0,t)

print(z)

#Step response
us = np.zeros(201) 
us[26:] = 2
ts = np.linspace(0,40,201)

#plot graph 


plt.plot(t,z[:,0],linewidth = 1, label = "dxdt")
plt.plot(t,z[:,1],'b-', label = "dydt")
plt.plot(ts,us,'r--', label = "Step")
plt.xlabel("Time")
plt.ylabel("y(t)")
plt.legend()
plt.show()


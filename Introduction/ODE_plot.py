#To solve differential equation and plot graph using ODEINT

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

def model(y,t,k):

    dydt = - k * y
    return dydt

#intital condition 
y0 = 6

#time 
t = np.linspace(0,20) 

#solve ode 
k1 = 0.1
y1 = odeint(model,y0,t,args=(k1,))
k2 = 0.2
y2 = odeint(model,y0,t,args=(k2,))
k3 = 0.3
y3 = odeint(model,y0,t,args=(k3,))

#plotting 

plt.plot(t,y1,'r',linewidth=2,label="k=0.1")
plt.plot(t,y2,'b',linewidth=1.5,label="k=0.2")
plt.plot(t,y3,'g',linewidth=1,label="k=0.3")
plt.xlabel('Time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
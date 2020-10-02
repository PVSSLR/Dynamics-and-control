#Problem 2 
# dy/dt = 1/5 * ( - y(t) + u(t) ) 
#Initial Condition y(0) = 1


import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint 

def model(y,t,u):
    if(t>10):
        u = 2
    else:
        u = 0

    dydt =(- y + u)/5 
    return dydt

#Initial Condition and time 
y0 = 1 
t = np.linspace(0,35 ) 

#Solve ODE 
u = 0
y = odeint(model,y0,t,args=(u,))

#plot 
plt.plot(t,y)
plt.xlabel("time")
plt.ylabel("y(t)")
plt.show()


 

    

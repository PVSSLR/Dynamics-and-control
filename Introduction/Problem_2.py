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
plt.plot(t,y,linewidth=3, label = r'$\frac{dx}{dt} = 3 * \exp(-t) $')
plt.plot([0,10,10,40],[0,0,2,2],linewidth=2, label = 'u(t)')

plt.xlabel("time")
plt.ylabel("y(t)")
plt.legend()
plt.show()


 

    

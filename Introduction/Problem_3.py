#Problem 3 
import numpy as np 
import matplotlib.pyplot as plt 
from  scipy.integrate import odeint 

def model1(x,t):
    dxdt = 3 * np.exp(-t)
    return dxdt

def model2(y,t):
    dydt = 3 - y 
    return dydt

#Initial Conditions for model 1 & 2 
x0 = 0             
y0 = 0

#time 
t = np.linspace(0,30)

#Solve ODE 
x = odeint(model1,x0,t)
y = odeint(model2,y0,t)

#plot
plt.plot(t,x,'r--',linewidth=2,label="dx/dt")
plt.xlabel("time")
plt.ylabel("x")
plt.legend()
plt.show()

plt.plot(t,y,'b-',linewidth=3,label="dy/dt")
plt.xlabel("time")
plt.ylabel("y")
plt.legend()
plt.show()


plt.plot(t,x,'r--',linewidth=2,label="dx/dt")
plt.plot(t,y,'b-',linewidth=1,label="dy/dt")
plt.xlabel("time")
plt.ylabel("x,y")
plt.legend()
plt.show()
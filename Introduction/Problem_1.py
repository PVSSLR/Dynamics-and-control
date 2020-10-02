# Problem 1 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import odeint

def model(y,t,k):
    dydt = -y + k 
    return dydt

# Initial condition y(0) = 0
y0 = 0 
# Time 
t = np.linspace(0,10) 
#Solving ODE
k = 1
y = odeint(model,y0,t,args=(k,))

#plotting 

plt.plot(t,y,label = "-y+1")
plt.xlabel("Time")
plt.ylabel("Y(t)")
plt.legend()
plt.show()

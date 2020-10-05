from scipy.integrate import odeint 
import matplotlib.pyplot as plt 
import numpy as np

us = np.zeros(201) 
us[26:] = 2
print(u)
ts = np.linspace(0,40,201)
plt.plot(ts,us)
plt.show()
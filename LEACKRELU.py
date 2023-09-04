import numpy as np
import matplotlib.pyplot as plt
def Leaky_relu(x):
    return np.maximum(0.01*x,x)

x=np.arange(-5,5,0.1)
y=Leaky_relu(x)
plt.plot(x,y)
plt.show()

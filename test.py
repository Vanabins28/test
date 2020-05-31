import matplotlib.pyplot as plt
import numpy as np 

#y = np.sin(x)
x = np.linspace(0,20,100)
y = np.sin(x)

plt.scatter(x,y)
plt.show()
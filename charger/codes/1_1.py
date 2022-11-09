import numpy as np
from matplotlib import pyplot as plt 

A_0 = 12 
t = np.linspace(0, 2/50, 1000)
x = A_0*np.abs(np.sin(2 *np.pi*50*t))

#plt.axhline(y = 0, label = "y = 0")

plt.plot(t, x)
plt.title("Plot of x{t) vs t")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid()

plt.savefig("../figs/1_1.pdf")
plt.show()

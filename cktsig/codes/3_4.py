import numpy as np
from matplotlib import pyplot as plt 

N = 1.5 * 1e6
t = np.linspace(0, 5 * 1e-6, 1000)
y = (2/3)*(1 + np.exp(-N*t))
X = np.loadtxt('3_4_output.dat')
plt.plot(t, y)
plt.plot(X[:,0], X[:,1], 'ro')
plt.grid(True)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.savefig("../figs/3_4.pdf")
plt.show()
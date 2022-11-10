import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def y(t):
    if t < 0: 
        return 0
    else:
        return 2/3 * (1 - np.exp(-1.5e6 * t))

def y_disc(n):
    if n < 0:
        return 0
    else:
        return 2/3 * (1 - (1 - 7.5e5 * 1e-7)**(n*1e7)/(1 + 7.5e5 * 1e-7)**(n*1e7))

yt = sp.vectorize(y)
yn = sp.vectorize(y_disc)

f = np.loadtxt('4_7_output.dat')
T = np.linspace(0, 5e-6, 40)

plt.plot(T, yt(T), label='$y(t)$')
plt.plot(f[:,0], f[:,1], 'o', mfc='g', mec='g', label='y(t) with ngspice')
plt.plot(T, yn(T), 'o', mfc='orange',label='$y(n)$')
plt.grid()
plt.legend()
plt.savefig('../figs/4_7.pdf')
plt.show()
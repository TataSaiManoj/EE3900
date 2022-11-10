import numpy as np
import matplotlib.pyplot as plt

def H(s):
    return (5 * 1e5)/(s + (1.5 * 1e6))

S = np.linspace((-4* 1e6), (1* 1e6), 100)

plt.plot(S, H(S))
plt.grid()
plt.title('Transfer Function')
plt.xlabel('$s$')
plt.ylabel('$H(s)$')
plt.savefig('./figs/4_3.pdf')
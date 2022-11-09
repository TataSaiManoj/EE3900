import numpy as np
import matplotlib.pyplot as plt

A_0 = 12
f = 50

def x(t):
    return A_0 * np.abs(np.sin(2 * np.pi * f * t))

def c_x(k, t):
    return np.exp(2j * np.pi * k * f * t)

def c(k):
    if k % 2:
        return 0
    else:
        return 2 * A_0 / (np.pi * (1 - k**2))

C = np.vectorize(c)

def c_x2(t):
    return np.sum([C(k) * c_x(k, t) for k in range(-100, 101)])

c_x2_vec = np.vectorize(c_x2)

t = np.linspace(-0.03, 0.03, 1000)
t2 = np.linspace(-0.03, 0.03, 100)

plt.plot(t, x(t), label='x(t)')
plt.plot(t2, np.real(c_x2_vec(t2)), 'o', label='fourier points')
plt.legend()
plt.savefig("./figs/2_3.pdf")
plt.show()



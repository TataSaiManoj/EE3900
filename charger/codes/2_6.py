import numpy as np
import matplotlib.pyplot as plt

A_0 = 12
f = 50

def x(t):
    return A_0 * np.abs(np.sin(2 * np.pi * f * t))

def a(k):
    if k < 0:
        return 0
    elif k == 0:
        return 2 * A_0 / np.pi
    elif k % 2 == 0:
        return 4 * A_0 / (np.pi * (1 - k**2))
    else:
        return 0

def e_cos(k, t):
    return np.cos(2 * np.pi * k * f * t)

a_vec = np.vectorize(a)

def a_sum(t):
    return np.sum([a_vec(k) * e_cos(k, t) for k in range(-100, 101)])

a_sum_vec = np.vectorize(a_sum)

t = np.linspace(-0.03, 0.03, 1000)
t2 = np.linspace(-0.03, 0.03, 100)

plt.plot(t, x(t))
plt.plot(t2, a_sum_vec(t2), 'o', markerfacecolor='red')
plt.legend()
plt.savefig("./figs/2_6.pdf")
plt.show()


# b(k) = 0 for all k

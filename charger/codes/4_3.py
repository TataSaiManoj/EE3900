import numpy as np
import matplotlib.pyplot as plt
import scipy

# Functions for the Fourier transform
def x(t):
    return 12*np.abs(np.sin(2*np.pi*50*t))

def h(t):
    return 100*np.sinc(100*t)

# Sampling rate
t=1e5

vec_h=scipy.vectorize(h, otypes=['double'])
vec_x=scipy.vectorize(x, otypes=['double'])

z=np.linspace(-1e5,1e5,t)
o=np.linspace(0,2e5,t)

# Convolution
y=np.convolve(vec_h(z),vec_x(z))
p=5*np.ones(100000)

# Plotting
plt.plot((5*np.pi/24)*y*2,label='simulation')
plt.plot(o,p,color="red",label="$5$V")
plt.legend()
plt.grid()
plt.savefig('figs/4_3.pdf')
plt.show()
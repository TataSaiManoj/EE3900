import numpy as np
import scipy.fftpack as fft
from matplotlib import pyplot as plt

# Initial amplitude and frequency
A = 12
f = 50

# Scale 
scl = 80

# DDF
def ddf(k):
    mag = 4*A/(np.pi*(1-k**2))
    plt.plot([f*k, f*k], [0, scl*np.abs(mag)], 'C1')
ddf_vec = np.vectorize(ddf)

# Fourier transform with numpy
ts = 5*1e-4
t = np.arange(-2/f, 2/f, ts)
sig = A*np.abs(np.sin(2*np.pi*f*t))
sig_fft = fft.fft(sig)
sampl_freq = fft.fftfreq(sig.size, d=ts)

# Plotting the transforms 
plt.plot(sampl_freq, np.abs(sig_fft), 'C0.')
ddf_vec([-4, -2, 0, 2, 4])

plt.grid()
plt.xlim(-4*f, 4*f)
plt.legend(['Simulation', 'Analysis'])
plt.savefig('../figs/3_8.pdf')
plt.show()

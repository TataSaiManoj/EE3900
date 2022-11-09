import numpy as np
import scipy.fftpack as fft
from matplotlib import pyplot as plt

# Fourier transform with scipy 
ts = 2*1e-2
sig = np.zeros(100)
sig[:50] = 1
sig_fft = fft.fftshift(fft.fft(sig))
sig_fft = np.abs(sig_fft)/max(np.abs(sig_fft))
sf = fft.fftshift(fft.fftfreq(sig.size, d=ts))

# Plotting the transforms
plt.plot(sf, sig_fft, '.')
plt.plot(sf, np.sinc(sf))
plt.legend(['Simulation', 'Analysis'])
plt.grid()
plt.savefig('../figs/3_9.pdf')
plt.show()
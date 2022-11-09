import numpy as np
import scipy.fftpack as fft
from matplotlib import pyplot as plt

# Rectangle function
def rect(x): 
    return np.where(np.abs(x) < 0.5, 1, 0)
rect = np.vectorize(rect, otypes=['double'])

# Fourier transform with scipy
ts = 2e-4
N = 100
mid = int(N/ts)
sig = np.sinc(np.arange(-N, N, ts))
sig_fft = fft.fftshift(fft.fft(sig))
sig_fft = np.abs(sig_fft)/np.abs(sig_fft[mid])
sf = fft.fftshift(fft.fftfreq(sig.size, d=ts))

# Plotting the transforms
plt.plot(sf, sig_fft, '.')
plt.plot(sf, rect(sf))
plt.legend(['Simulation', 'Analysis'], loc="best")
plt.grid()
plt.xlim(-1.2, 1.2)
plt.savefig('../figs/3_10.pdf')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1], dtype=float)
x = np.pad(x, (0,2), 'constant', constant_values=(0))
X = np.fft.fft(x)

plt.stem(np.real(X), use_line_collection=True)
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('FFT after zero padding $\mathbf{x}$')
plt.grid()

#If using termux
plt.savefig('./figs/7.12.pdf')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
plt.show()
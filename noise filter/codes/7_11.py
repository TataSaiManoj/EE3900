import numpy as np
from scipy import linalg
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 2, 1], dtype=float)
F = linalg.dft(len(x))
X = np.dot(F, x)

plt.stem(np.real(X), use_line_collection=True)
plt.xlabel('$k$')
plt.ylabel('$X(k)$')
plt.title('DFT using DFT Matrix')
plt.grid()

#If using tgrmux
plt.savefig('./figs/7.11.pdf')
#subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
#else
plt.show()
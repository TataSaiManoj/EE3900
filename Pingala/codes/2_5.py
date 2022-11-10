import numpy as np
from matplotlib import pyplot as plt 

x = [1, 1]
y = [1]
N = 20

for i in range(2, N+1): x.append(x[i-1] + x[i-2])

for i in range(1, N):
    y.append(x[i-1] + x[i+1])

plt.stem(y, use_line_collection=True)
plt.title("Stem plot for y[n]")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.savefig("../figs/2_5.pdf")
plt.show()

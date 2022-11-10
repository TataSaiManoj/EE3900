import numpy as np 
from matplotlib import pyplot as plt

x = [1, 1]
N = 20

for i in range(2, N+1): x.append(x[i-1] + x[i-2])

# stem plot for x[n]
plt.stem(x, use_line_collection=True)
plt.title("Stem plot for x[n]")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.savefig("../figs/2_2.pdf")
plt.show()

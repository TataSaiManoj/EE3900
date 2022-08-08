import numpy as np 

x = np.array([2, -1]).T
h = np.array([-1, 2, 1]).T

m = x.size
n = h.size

toeplitz = np.zeros((n + m - 1, n))

# generating toeplitz matrix 
for i in range(0, n + m - 1):
	for j in range(0, n):
		if(abs(j-i) < m and j <= i):
			toeplitz[i][j] = x[abs(j-i)]
		else:
			toeplitz[i][j] = 0
		
print(toeplitz)
print("Output Matrix : ", toeplitz @ h)
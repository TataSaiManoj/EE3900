import numpy as np 
from math import isclose

coeff = [1, -1, -1]
roots = np.roots(coeff)
alpha = roots[0]
beta = roots[1]
n = len(coeff) -1 
a = [0]
b = [0]
N = 50
sum = 0

for i in range(1, N+3): a.append((pow(alpha, i) - pow(beta, i))/(alpha - beta))
for i in range(1, N): b.append(a[i-1] + a[i+1])

# 1.1

for i in range(1, n+1): sum += a[i]
print("1.1 is", isclose(sum, a[n+2] - 1))
print("The LHS summation is : ", (sum), " and RHS is : ", round(a[n+2] - 1))

# 1.2

sum = 0

for i in range(1, N): sum += (a[i]/10**i)
print("1.2 is", isclose(sum, 10/89))
print("The sum of the given infinite summation is : ", round(sum, 5))
print("The sum using GP formula is ", round(10/89, 5))

# 1.3

b_prime = [0]
r = np.random.randint(1, N - 1)
for i in range(1, N): b_prime.append(alpha**i + beta**i)

print("Given option is ", isclose(b[r], b_prime[r]))
print("LHS is : ", [round(item, 3) for item in b])
print("RHS is ", [round(item, 3) for item in b_prime])

# 1.4

for i in range(1, N): sum += (b[i]/(10**i))
print("Given option is ", isclose(sum, 8/89))
print("The sum of the given infinite summation is : ", sum)
print("The sum using GP formula is ", 10/89)








import numpy as np

def kernel_function(x1, x2):
    s = 0

    for i, j in zip(x1, x2):
        p = i * j
        s += p

    return s
	

x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])

result = kernel_function(x1, x2)
print(result)

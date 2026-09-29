import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
	# Your code here
	return x.mean(axis=(0, 1))
	pass
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
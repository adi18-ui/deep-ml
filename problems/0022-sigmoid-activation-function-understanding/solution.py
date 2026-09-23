import math

def sigmoid(z: float) -> float:
	#Your code here
	exp = math.exp(-z)
	result = 1/(1+ exp)
	return result

sigmoid(0)
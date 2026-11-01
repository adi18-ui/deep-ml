import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
	# Your code here

	mse_values = []

	weights = initial_weights.copy()
	bias = initial_bias

	for epoch in range(epochs):
		z = features @ weights + bias 
		pred = 1 / (1 + np.exp(-z))

		mse = np.mean((labels - pred) ** 2)
		mse_values.append(mse)

		n = len(labels)

		dL_dpred = (2 / n) * (pred - labels)
		dpred_dz = pred * (1 - pred)
		dL_dz = dL_dpred * dpred_dz

		weight_gradient = features.T @ dL_dz
		bias_gradient = np.sum(dL_dz)
	
		weights = weights - learning_rate * weight_gradient
		bias = bias - learning_rate * bias_gradient

	return (
    	np.round(weights, 4).tolist(),
    	round(float(bias), 4),
    	np.round(mse_values, 4).tolist()
	)
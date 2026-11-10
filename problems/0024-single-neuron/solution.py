import math
import numpy as np
def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    features = np.asarray(features, dtype=float)
    labels = np.asarray(labels, dtype=float)
    weights = np.asarray(weights, dtype=float)

    z = features @ weights + bias
    pred = 1 / (1 + np.exp(-z))

    mse = np.mean((labels - pred) ** 2)

    return pred, mse
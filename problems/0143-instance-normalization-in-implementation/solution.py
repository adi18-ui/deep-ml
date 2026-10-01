import numpy as np

def instance_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
    """
    Perform Instance Normalization over a 4D tensor X of shape (B, C, H, W).
    gamma: scale parameter of shape (C,)
    beta: shift parameter of shape (C,)
    epsilon: small value for numerical stability
    Returns: normalized array of same shape as X
    """
    # TODO: Implement Instance Normalization

    mean = np.mean(X, axis=(2, 3), keepdims=True)
    variance = np.var(X, axis=(2, 3), keepdims=True)

    normalized_X = (X - mean) / np.sqrt(variance + epsilon)

    scaled_X = gamma * (normalized_X) + beta
    return scaled_X


    pass
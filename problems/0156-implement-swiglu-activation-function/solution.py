import numpy as np

def SwiGLU(x: np.ndarray) -> np.ndarray:
    d = x.shape[-1] // 2

    # Split columns into two equal halves
    x1 = x[:, :d]
    x2 = x[:, d:]

    sigmoid_x2 = 1 / (1 + np.exp(-x2))

    # Swish(x2) = x2 * sigmoid(x2)
    swish_x2 = x2 * sigmoid_x2

    # SwiGLU(x) = x1 * Swish(x2)
    output = x1 * swish_x2

    return np.round(output, 4)
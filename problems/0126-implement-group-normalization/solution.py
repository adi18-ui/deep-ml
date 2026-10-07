import numpy as np

def group_normalization(
    X: np.ndarray,
    gamma: np.ndarray,
    beta: np.ndarray,
    num_groups: int,
    epsilon: float = 1e-5
) -> np.ndarray:

    B, C, H, W = X.shape

    if C % num_groups != 0:
        raise ValueError("Number of channels must be divisible by num_groups")

    channels_per_group = C // num_groups

    # (B, C, H, W) → (B, G, C/G, H, W)
    X_grouped = X.reshape(
        B, num_groups, channels_per_group, H, W
    )

    mean = np.mean(X_grouped, axis=(2, 3, 4), keepdims=True)

    variance = np.var(X_grouped, axis=(2, 3, 4), keepdims=True)

    normalized = ((X_grouped - mean) / np.sqrt(variance + epsilon))

    # Restore original shape
    normalized = normalized.reshape(B, C, H, W)

    gamma = np.asarray(gamma).reshape(1, C, 1, 1)
    beta = np.asarray(beta).reshape(1, C, 1, 1)

    return gamma * normalized + beta


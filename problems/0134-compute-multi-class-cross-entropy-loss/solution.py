import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    # Your code here

    safe_probs = np.clip(predicted_probs, epsilon, 1 - epsilon)
    log_probs = np.log(safe_probs)
    selected_log_probs = true_labels * log_probs
    total_loss = -np.sum(selected_log_probs)
    average_loss = total_loss / predicted_probs.shape[0]

    return average_loss
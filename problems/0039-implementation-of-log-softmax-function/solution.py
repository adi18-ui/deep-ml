import numpy as np
import math


def log_softmax(scores: list) -> np.ndarray:
    scores = np.array(scores)
    max_x = max(scores)

    log_sum_exp = math.log(
        np.sum(np.exp(scores - max_x))
    )

    result = []

    for score in scores:
        result.append(score - max_x - log_sum_exp)

    return np.round(np.array(result), 4)

A = np.array([1, 2, 3])
log_softmax(A)
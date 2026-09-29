import numpy as np
def mae(y_true, y_pred):
    return float(np.mean(np.abs(y_true - y_pred)))

y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])

mae(y_true, y_pred)
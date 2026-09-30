import numpy as np
def divide_on_feature(X, feature_i, threshold):
    greater = []
    lower = []

    for row in X:
        if row[feature_i] >= threshold:
            greater.append(row)
        else:
            lower.append(row)

    greater = np.array(greater)
    lower = np.array(lower)

    return [greater, lower]
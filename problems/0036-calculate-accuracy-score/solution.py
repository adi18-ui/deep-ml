import numpy as np

def accuracy_score(y_true, y_pred):
    count = 0
    for i,j in zip(y_true, y_pred):
        if i == j:
            count += 1
        else:
            pass

    return count/len(y_true)


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = accuracy_score(y_true, y_pred)

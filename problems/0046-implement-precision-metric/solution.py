import numpy as np

def precision(y_true, y_pred):

    denominator = 0
    for i in y_pred:
        if i == 1:
            denominator += 1

    numerator = 0
    for m,n in zip(y_true, y_pred):
        if m == 1 and n == 1:
            numerator += 1

    if denominator == 0:
		return 0
	else:
		return numerator/denominator

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
output = precision(y_true, y_pred)


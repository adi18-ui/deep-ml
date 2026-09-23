import numpy as np

def batch_iterator(X, y=None, batch_size=1):
    batches = []

    for start in range(0, len(X), batch_size):
        end = start + batch_size

        if y is not None:
            batches.append([
                X[start:end],
                y[start:end]
            ])
        else:
            batches.append(X[start:end])

    return batches


X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
batch_iterator(X, y, batch_size)
import numpy as np

def to_categorical(x, n_col=None):

    if n_col is None:
        n_col = np.max(x) + 1

    empty_matrix = np.zeros((len(x), n_col))

    for row_index, class_label in enumerate(x):
        empty_matrix[row_index, class_label] = 1

    return empty_matrix
	
x = np.array([0, 1, 2])
output = to_categorical(x)

import numpy as np


def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    
    mean_x = np.mean(data, axis=0)
    std_x = np.std(data, axis=0)

    max_x = np.max(data, axis=0)
    min_x = np.min(data, axis=0)

    standardized_data = (data - mean_x) / std_x
    normalized_data = (data - min_x) / (max_x - min_x)

    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)

    return standardized_data, normalized_data


data = np.array([[1, 2], [3, 4], [5, 6]])

standardized_data, normalized_data = feature_scaling(data)

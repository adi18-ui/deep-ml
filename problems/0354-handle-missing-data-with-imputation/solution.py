import numpy as np

def impute_missing_data(
    data: np.ndarray,
    strategy: str = "mean"
) -> np.ndarray:

    result = data.astype(float).copy()

    for col_index in range(result.shape[1]):
        column = result[:, col_index]
        missing_mask = np.isnan(column)

        if not np.any(missing_mask):
            continue

        valid_values = column[~missing_mask]

        if len(valid_values) == 0:
            continue

        if strategy == "mean":
            replacement_value = np.mean(valid_values)

        elif strategy == "median":
            replacement_value = np.median(valid_values)

        elif strategy == "mode":
            values, counts = np.unique(
                valid_values,
                return_counts=True
            )
            mode_index = np.argmax(counts)
            replacement_value = values[mode_index]

        else:
            raise ValueError("Strategy must be 'mean', 'median', or 'mode'")

        column[missing_mask] = replacement_value

    return result
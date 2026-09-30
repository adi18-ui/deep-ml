import numpy as np

def convert_range(values: np.ndarray, c: float, d: float) -> np.ndarray:
    """
    Shift and scale values from their original range [min, max] to
    a target [c, d] range.
    """
    a = np.min(values)
    b = np.max(values)
    
    # Scale to [0, 1] then shift to [c, d]
    scaled = c + ((values - a) / (b - a)) * (d - c)
    
    return scaled.astype(float)
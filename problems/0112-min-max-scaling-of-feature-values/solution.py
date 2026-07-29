def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    a = []    # new empty list
    x_max = max(x)
    x_min = min(x)
    for i in range(len(x)):
        a.append((x[i]-x_min)/(x_max-x_min))
    
    return a
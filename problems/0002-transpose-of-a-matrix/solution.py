def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    rows = len(a)
    columns = len(a[0])
    new_l = []
    for i in a:
        transpose = [
        [0 for _ in range(rows)]
        for _ in range(columns)
    ]

    for i in range(rows):
        for j in range(columns):
            transpose[j][i] = a[i][j]
    
    return transpose

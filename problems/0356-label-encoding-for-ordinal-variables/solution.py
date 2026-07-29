def label_encode_ordinal(values: list, order: list) -> list:
    """
    Encode ordinal categorical values to integers based on specified order.
    
    Args:
        values: List of categorical values to encode
        order: List specifying the order of categories from lowest (0) to highest
    
    Returns:
        List of integers representing the encoded values
    """
    cat_order = {}
    for i,key in enumerate(order):
        cat_order[key] = i
    # print(cat_order)

    val_lst = []
    for i in values:
        if i in cat_order:
            val_lst.append(cat_order[i])
        else:
            val_lst.append(-1)
         
    
    return val_lst
    
    pass
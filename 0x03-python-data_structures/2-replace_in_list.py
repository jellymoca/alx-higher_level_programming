#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace my_list[idx] with element like in C.

    Args:
        my_list (list): list to perform replacement on
        idx (int): Index of old element
        element: New element

    Returns:
        New list, or original list if idx is >range // <0
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list

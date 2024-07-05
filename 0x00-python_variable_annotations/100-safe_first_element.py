#!/usr/bin/env python3
"""
Module: safe_first_element

Defines a function to safely retrieve the
first element from a list of unknown types.
"""

from typing import Sequence, Union


def safe_first_element(lst: Sequence) -> Union[None, object]:
    """
    Safely retrieves the first element from the input list if it exists.

    Args:
        lst (Sequence): Input list of elements of unknown type.

    Returns:
        Union[None, object]: The first element of the input list, or None if
        the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None

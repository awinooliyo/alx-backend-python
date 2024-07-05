#!/usr/bin/env python3

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains an element from lst
    paired with its length.

    Args:
        lst (Iterable[Sequence]): Input iterable containing sequences (e.g.,
            list, tuple, string).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
            an element from lst paired with its length.
    """
    return [(i, len(i)) for i in lst]

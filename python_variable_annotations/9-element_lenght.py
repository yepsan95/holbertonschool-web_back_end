#!/usr/bin/env python3
"""
Defines a type-annotated function that takes a list as an argument
and returns a list of tuples where the first element of each tuple
is an element of the original list and the second is its length.
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of each element and its length"""
    return [(i, len(i)) for i in lst]

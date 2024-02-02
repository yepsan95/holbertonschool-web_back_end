#!/usr/bin/env python3
"""Defines a type-annotated function.
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Type-annotated funciont that returns a list"""
    if lst:
        return lst[0]
    else:
        return None

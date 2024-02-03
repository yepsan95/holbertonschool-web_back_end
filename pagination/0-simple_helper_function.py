#!/usr/bin/env python3
"""Defines a function index_range that returns and index range
of items on a specific page using pagination."""
from typing import Literal, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns an index range of items on a specific page

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.
    """
    start_index = (page_size) * (page - 1)
    end_index = (page_size) * page
    return (start_index, end_index)

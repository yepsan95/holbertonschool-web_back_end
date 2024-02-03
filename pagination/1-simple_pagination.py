#!/usr/bin/env python3
"""Defines a function index_range that returns and index range
of items on a specific page using pagination."""
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Gets all the elements in a page and returns them
        as a list of lists.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        csv_data = self.dataset()
        range = index_range(page, page_size)
        start_index = range[0]
        end_index = range[1]
        page_contents = csv_data[start_index:end_index]
        return page_contents


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns an index range of items on a specific page

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.
    """
    start_index = (page_size) * (page - 1)
    end_index = (page_size) * page
    return (start_index, end_index)

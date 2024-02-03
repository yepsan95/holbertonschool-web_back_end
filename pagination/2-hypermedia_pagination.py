#!/usr/bin/env python3
"""Defines a function index_range that returns and index range
of items on a specific page using pagination."""
import csv
import math
from typing import List, Literal, Optional, Tuple, TypedDict


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

    GetPageReturn = TypedDict('GetPageReturn', {"page_size": int,
                                                "page": int,
                                                "data": List[List],
                                                "next_page": Optional[int],
                                                "prev_page": Optional[int],
                                                "total_pages": int
                                                })

    def get_hyper(self, page: int = 1, page_size: int = 10) -> GetPageReturn:
        """Returns hypermedia metadata of the dataset.

        Args:
            page (int): The page number.
            page_size (int): The number of items per page.
        """
        data = self.get_page(page, page_size)
        total_len = len(self.__dataset)
        total_pages = math.ceil(total_len / page_size)
        item_count = page * page_size
        return_value = {}
        return_value["page_size"] = page_size if item_count < total_len else 0
        return_value["page"] = page
        return_value["data"] = data
        return_value["next_page"] = page + 1 if page < total_pages else None
        return_value["prev_page"] = page - 1 if page > 1 else None
        return_value["total_pages"] = total_pages

        return return_value


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns an index range of items on a specific page

    Args:
        page (int): The page number.
        page_size (int): The number of items per page.
    """
    start_index = (page_size) * (page - 1)
    end_index = (page_size) * page

    return (start_index, end_index)

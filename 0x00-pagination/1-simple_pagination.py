#!/usr/bin/env python3
""" A module that paginates the data from a csv file """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ The function """
    end_index: int = page * page_size
    start_index: int = end_index - page_size
    return start_index, end_index


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
        """Paginate the returned data
        """
        assert type(page) is int
        assert page >= 0
        assert type(page_size) is int
        assert page_size >= 0

        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]


if __name__ == "__main__":
    x = Server()
    x.dataset()
    x.get_page()

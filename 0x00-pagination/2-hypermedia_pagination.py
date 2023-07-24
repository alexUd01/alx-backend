#!/usr/bin/env python3
""" A module that the data from a csv file """
import csv
import math
from typing import Dict, List, Tuple


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
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0

        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Does stuff not yet known
        """
        # Compute next_page
        if len(self.get_page(page + 1, page_size)) <= 0:
            next_page = None
        else:
            next_page = page + 1
        # Compute prev_page
        if page < 1 or page_size > len(self.__dataset):
            prev_page = None
        else:
            prev_page = page - 1

        page_data = self.get_page(page, page_size)
        data = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': math.ceil(len(self.__dataset) / page_size)
        }
        return data


if __name__ == "__main__":
    x = Server()
    x.dataset()
    x.get_page()

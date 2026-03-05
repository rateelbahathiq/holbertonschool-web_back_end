#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: truncated_dataset[i] for i in range(len(truncated_dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Deletion-resilient pagination.

        Returns a dict:
        - index: current start index
        - next_index: index to use for next call
        - page_size: number of items returned
        - data: list of rows
        """
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.indexed_dataset()
        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < len(self.dataset())

        data: List[List] = []
        current = index

        while len(data) < page_size and current < len(self.dataset()):
            if current in dataset:
                data.append(dataset[current])
            current += 1

        return {
            "index": index,
            "next_index": current,
            "page_size": len(data),
            "data": data,
        }

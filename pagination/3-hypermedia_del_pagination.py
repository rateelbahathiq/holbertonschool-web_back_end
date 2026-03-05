#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class used to paginate a dataset of popular baby names.
    It supports deletion-resilient pagination.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize dataset and indexed dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache the dataset from the CSV file."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]

            # Remove the header row
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Create a dictionary where keys are row indexes
        and values are the corresponding dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()

        
            truncated_dataset = dataset[:1000]

    
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a page of data starting from a given index.
        """

        # Validate the starting index
        assert (type(index) is int and index <= len(self.__indexed_dataset))

        data = []
        next_index = index
        current_count = 0

        indexed_dataset = self.indexed_dataset()
        max_index = len(indexed_dataset)

        # Collect page_size items, skipping deleted indexes
        while current_count < page_size and next_index < max_index:
            if next_index in indexed_dataset:
                data.append(indexed_dataset[next_index])
                current_count += 1
            next_index += 1

        # Return pagination metadata
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }

#!/usr/bin/env python3
"""A module that contains a class `LRUCache` that inherits from BaseCaching
and is a caching system:

INSTRUCTIONS:
- You must use `self.cache_data` - dictionary from the parent class BaseCaching
- You can overload `def __init__(self):` but don’t forget to call the
  parent init: `super().__init__()
- def put(self, key, item):
  - Must assign to the dictionary `self.cache_data` the `item` value for
    the key `key`.
  - If `key` or `item` is None, this method should not do anything.
  - If the number of items in `self.cache_data` is higher
    than `BaseCaching.MAX_ITEMS`:
    - you must discard the least recently used item (LRU algorithm)
    - you must print `DISCARD:` with the key discarded and following
      by a newline
- def get(self, key):
  - Must return the value in `self.cache_data` linked to key.
  - If `key` is None or if the `key` doesn’t exist in `self.cache_data`,
    return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


def get_key_index(key, lst):
    """ A helper function """
    for i in range(len(lst)):
        if key in lst[i].keys():
            return i
    return None


def get_other_key(known_key, d):
    """ A helper function """
    for key in d.keys():
        if key != known_key:
            return key


def get_next_pop(start_key, start_idx, lst):
    """ A helper function """
    for i in range(start_idx, len(lst)):
        k = list(lst[i].keys())[0]
        if lst[i][k] <= lst[start_idx - 1][start_key]:
            return i, k


class LRUCache(BaseCaching):
    """ The class """

    def __init__(self):
        """ Initializations """
        super().__init__()
        self.__nb_items = 0
        self.__keys_lst = [{} for _ in range(self.MAX_ITEMS)]
        self.__next_pop_idx_n_key = None

    def put(self, key, item):
        """ Insert data into cache storage """
        if key is None or item is None:
            return
        # 1. If key already exists
        idx = get_key_index(key, self.__keys_lst)
        if idx is not None:
            self.cache_data[key] = item
            self.__keys_lst[idx][key] += 1
            self.__next_pop_idx_n_key = get_next_pop(key, idx + 1, self.__keys_lst)
            return

        # 2. If the key does not exist
        self.cache_data[key] = item

        if self.__next_pop_idx_n_key is not None:
            i, k = self.__next_pop_idx_n_key
            print('DISCARD: {}'.format(k))
            del self.cache_data[k]
            self.__keys_lst[i] = {key: 1}
            self.__next_pop_idx_n_key = get_next_pop(k, i + 1, self.__keys_lst)
            return

        curr_idx = self.__nb_items % self.MAX_ITEMS
        self.__keys_lst[curr_idx][key] = 1  # may be a dict with 2 k:v pairs

        # 3. Insertion after MAX_ITEMS exceeded
        if self.__nb_items >= self.MAX_ITEMS:
            # remove old data from dict with 2 k:v pairs
            if len(self.__keys_lst[curr_idx].keys()) == 2:
                other_key = get_other_key(key, self.__keys_lst[curr_idx])
                del self.__keys_lst[curr_idx][other_key]
                print('DISCARD: {}'.format(other_key))
                del self.cache_data[other_key]
        self.__nb_items += 1

    def get(self, key):
        """ Retrieve data stored in cache """
        if key not in self.cache_data.keys():
            return
        for d in self.__keys_lst:
            if key in d.keys():
                d[key] += 1
        return self.cache_data.get(key)

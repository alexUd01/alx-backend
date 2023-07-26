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


class LRUCache(BaseCaching):
    """ The class """

    def __init__(self):
        """ Initializations """
        super().__init__()
        self.__nb_items = 0
        self.__keys_lst = []

    def put(self, key, item):
        """ Insert data into cache storage """
        if key is None or item is None:
            return
        # 1. If key already exists
        if key in self.__keys_lst:
            self.cache_data[key] = item
            for i in range(self.__keys_lst.index(key), self.MAX_ITEMS - 1):
                self.__keys_lst[i] = self.__keys_lst[i + 1]
            self.__keys_lst[-1] = key
            return

        # 2. If the key does not exist
        self.cache_data[key] = item
        self.__keys_lst.append(key)

        # 3. Insertion after MAX_ITEMS exceeded
        if self.__nb_items >= self.MAX_ITEMS:
            key_to_rm = self.__keys_lst[0]
            self.__keys_lst = self.__keys_lst[1:]
            print('DISCARD: {}'.format(key_to_rm))
            del self.cache_data[key_to_rm]

        self.__nb_items += 1

    def get(self, key):
        """ Retrieve data stored in cache """
        if key not in self.__keys_lst:
            return
        for i in range(self.__keys_lst.index(key), self.MAX_ITEMS - 1):
            self.__keys_lst[i] = self.__keys_lst[i + 1]
        self.__keys_lst[-1] = key
        return self.cache_data.get(key)

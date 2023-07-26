#!/usr/bin/env python3
"""A module that contains a class `MRUCache` that inherits from BaseCaching
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
    - you must discard the most recently used item (LRU algorithm)
    - you must print `DISCARD:` with the key discarded and following
      by a newline
- def get(self, key):
  - Must return the value in `self.cache_data` linked to key.
  - If `key` is None or if the `key` doesn’t exist in `self.cache_data`,
    return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ The class """

    def __init__(self):
        """ Initializations """
        super().__init__()
        self.__nb_items = 0
        self.__mru = None

    def put(self, key, item):
        """ Insert data into cache storage """
        if key is None or item is None:
            return
        if key in self.cache_data:  # key already exists - just update value
            self.cache_data[key] = item
            self.__mru = key
            return

        # Key does not exist
        former_mru = self.__mru
        self.cache_data[key] = item
        self.__mru = key

        # max_items exceeded
        if self.__nb_items >= self.MAX_ITEMS:
            if former_mru is not None:
                print('DISCARD: {}'.format(former_mru))
                del self.cache_data[former_mru]

        self.__nb_items += 1

    def get(self, key):
        """ Retrieve data stored in cache """
        if key not in self.cache_data.keys():
            return
        self.__mru = key
        return self.cache_data.get(key)

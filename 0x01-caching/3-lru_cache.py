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
        self.__keys = {}
        self.__nb_items = 0

    def put(self, key, item):
        """ Insert data into cache storage """
        if key is None or item is None:
            return
        if key in self.__keys.keys():  # IF KEY EXISTS (update the value stored)
            self.__keys[key] += 1
            self.cache_data[key] = item
            return

        # KEY DOES NOT EXIST
        try:  # get the least recently used item
            _min = min(self.__keys.values())
        except ValueError:  # List `self.__keys.values()` is empty
            _min = 0

        self.__keys[key] = 1
        self.cache_data[key] = item
        # remove least used item from cache
        if self.__nb_items >= self.MAX_ITEMS:
            former_key = None
            for k in self.cache_data.keys():
                if self.__keys[k] <= _min and k != key:
                    former_key = k
            print('DISCARD: {}'.format(former_key))
            del self.cache_data[former_key]
        self.__nb_items += 1

    def get(self, key):
        """ Retrieve data stored in cache """
        return self.cache_data.get(key)

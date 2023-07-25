#!/usr/bin/env python3
""" A module that contains a class LIFOCache that inherits from
BaseCaching and is a caching system.

INSTRUCTIONS:
- You must use self.cache_data - dictionary from the parent class BaseCaching
- You can overload `def __init__(self):` but don't forget to call the
  parent init: super().__init()
- def put(self, key, item):
  - Must assign to the dictionary `self.cache_data` the `item` value for
    the key `key`.
  - If `key` or `item` is None, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than
    BaseCaching.MAX_ITEMS:
    - you must discard the last item put in cache (LIFO algorithm)
    - you must print `DISCARD:` with the key discarded and following by
      a newline
- def get(self, key):
  - Must return the value in self.cache_data linked to key.
  - If `key` is None or if the `key` doesn’t exist in `self.cache_data`,
    return None
"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ The class """

    def __init__(self):
        """ Initializations """
        super().__init__()
        self.__keys = [None for _ in range(self.MAX_ITEMS)]
        self.__nb_items = 0

    def put(self, key, item):
        """ Insert data into cache storage """
        if key is None or item is None:
            return
        if key in self.__keys:  # Update value stored
            self.cache_data[key] = item
            return

        q_index = self.__nb_items % self.MAX_ITEMS
        former_key = self.__keys[q_index]
        self.__keys[q_index] = key
        self.cache_data[key] = item
        self.__nb_items += 1
        # remove previous item from cache
        if former_key is not None:
            print('DISCARD: {}'.format(former_key))
            del self.cache_data[former_key]

    def get(self, key):
        """ Retrieve data stored in cache """
        return self.cache_data.get(key)

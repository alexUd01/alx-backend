#!/usr/bin/env python3
"""A module that contains a class `LIFOCache` that inherits from BaseCaching
and is a caching system:

INSTRUCTIONS:
- You must use `self.cache_data` - dictionary from the parent class BaseCaching
- You can overload def __init__(self): but don’t forget to call the
  parent init: `super().__init__()`
- def put(self, key, item):
  - Must assign to the dictionary `self.cache_data` the item value for
    the key `key`.
  - If `key` or `item` is None, this method should not do anything.
  - If the number of items in `self.cache_data` is higher than
    `BaseCaching.MAX_ITEMS`:
    - you must discard the last item put in cache (LIFO algorithm)
    - you must print `DISCARD`: with the key discarded and following by
      a newline
- def get(self, key):
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is None or if the `key` doesn’t exist in `self.cache_data`,
    return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ The class """

    def __init__(self):
        """ Initializations """
        super().__init__()
        self.__keys = [None for _ in range(self.MAX_ITEMS)]
        self.__prev_key = None
        self.__nb_items = 0

    def put(self, key, item):
        """ Insert data into cache storage """
        if key is None or item is None:
            return
        if key in self.__keys:  # IF KEY EXISTS (update the value stored)
            self.__prev_key = key
            self.cache_data[key] = item
            return

        # KEY DOES NOT EXIST
        self.__keys[self.__nb_items % self.MAX_ITEMS] = key
        self.cache_data[key] = item
        former_key = self.__prev_key
        self.__prev_key = key
        # remove previous item from cache
        if self.__nb_items >= self.MAX_ITEMS and former_key is not None:
            print('DISCARD: {}'.format(former_key))
            del self.cache_data[former_key]
        self.__nb_items += 1

    def get(self, key):
        """ Retrieve data stored in cache """
        return self.cache_data.get(key)

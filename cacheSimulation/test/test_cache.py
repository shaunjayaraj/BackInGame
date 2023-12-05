import sys
import os
current_working_directory = os.getcwd()

sys.path.append('/Users/shaunjayaraj/Dropbox/projects/BackInGame/cacheSimulation/src')

import unittest
import cache

class Test_cache_miss(unittest.TestCase):
    def test_hit(self):
        cache.acceptRequests(7)
        cache.processRequests()
        self.assertEqual(-1, cache.getPage(77), "77 should not exist in the cache")

class Test_cache_hit(unittest.TestCase):
    def test_hit(self):
        cache.acceptRequests(7)
        cache.processRequests()
        self.assertEqual(7, cache.getPage(7), "7 should exist in the cache")


if __name__ == '__main__':
    unittest.main()

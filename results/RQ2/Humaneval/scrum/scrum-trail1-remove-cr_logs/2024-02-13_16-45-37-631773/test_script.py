from typing import List, Optional
import heapq

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_heap = [(-len(s), s) for s in strings]
    heapq.heapify(max_heap)
    return heapq.heappop(max_heap)[1]
import unittest

class Test(unittest.TestCase):
    def test_longest_empty_list(self):
        self.assertIsNone(longest([]))

    def test_longest_single_character_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_longest_multiple_character_strings(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

if __name__ == '__main__':
    unittest.main()
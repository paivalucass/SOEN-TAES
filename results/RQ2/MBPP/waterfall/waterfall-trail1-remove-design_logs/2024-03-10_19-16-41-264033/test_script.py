def count_Occurrence(tup, lst):
    if not isinstance(tup, tuple) or not isinstance(lst, list):
        raise ValueError("Input must be a tuple and a list")

    count = 0
    for item in lst:
        count += tup.count(item)
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_Occurrence(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'), ['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()
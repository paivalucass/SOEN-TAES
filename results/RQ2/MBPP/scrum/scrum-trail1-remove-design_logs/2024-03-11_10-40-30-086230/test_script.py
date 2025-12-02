def count_Occurrence(tup, lst):
    count = 0
    for elem in lst:
        count += tup.count(elem)
    return count
import unittest

class Test(unittest.TestCase):
    def test_count_Occurrence(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()
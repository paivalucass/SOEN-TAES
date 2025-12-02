def count_Occurrence(tup, lst):
    count = 0
    for item in lst:
        count += tup.count(item)
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()
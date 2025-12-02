def count_Occurrence(tup, lst):
    if not isinstance(tup, tuple) or not isinstance(lst, list) or not tup or not lst:
        return 0
    result = 0
    for item in lst:
        result += tup.count(item)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b'] ), 3)

if __name__ == '__main__':
    unittest.main()
def count_Occurrence(tup, lst):
    count_dict = {}
    for item in lst:
        count_dict[item] = tup.count(item)
    return sum(count_dict.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()
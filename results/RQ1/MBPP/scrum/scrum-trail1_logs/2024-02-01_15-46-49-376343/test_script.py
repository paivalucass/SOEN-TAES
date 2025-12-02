def count_occurrence(tup, lst):
    if not isinstance(tup, tuple) or not isinstance(lst, list):
        raise TypeError("Input should be a tuple and a list")

    count_dict = dict(Counter(tup))
    result = sum(count_dict.get(elem, 0) for elem in lst)

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_Occurrence(('a', 'a', 'c', 'b', 'd'),['a', 'b']), 3)

if __name__ == '__main__':
    unittest.main()
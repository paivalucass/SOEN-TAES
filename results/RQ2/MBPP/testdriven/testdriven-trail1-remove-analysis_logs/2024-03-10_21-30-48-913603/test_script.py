def _sum(arr):
    '''Write a python function to find the sum of an array.
    assert _sum([1, 2, 3]) == 6'''

    return sum(arr)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

if __name__ == '__main__':
    unittest.main()
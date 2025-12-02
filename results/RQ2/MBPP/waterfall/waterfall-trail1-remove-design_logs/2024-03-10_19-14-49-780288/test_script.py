def max_Product(arr):
    arr.sort()
    n = len(arr)

    if n < 2:
        return "Array should have at least 2 elements"

    max_pair = (arr[-2], arr[-1])
    return max_pair
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7, 8))

if __name__ == '__main__':
    unittest.main()
def max_product(arr):
    arr.sort()
    n = len(arr)
    if n < 2:
        raise ValueError('Error: Single element input array')
    if n == 0:
        raise ValueError('Error: Empty input array')
    if arr[-1] <= 0:
        return (arr[-2], arr[-1])
    else:
        return (arr[-1], arr[-2])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()
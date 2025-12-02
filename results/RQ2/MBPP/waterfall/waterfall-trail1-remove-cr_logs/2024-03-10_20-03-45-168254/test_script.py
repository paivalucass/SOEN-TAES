def max_product(arr):
    sorted_arr = sorted(arr)
    return (sorted_arr[-1], sorted_arr[-2]) if sorted_arr[-2] >= 0 else (sorted_arr[-1], sorted_arr[0])
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()
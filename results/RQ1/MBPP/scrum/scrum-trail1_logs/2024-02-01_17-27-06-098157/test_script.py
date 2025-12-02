def max_Product(arr):
  arr_copy = arr.copy()
  arr_copy.sort()
  max1 = arr_copy[-1]
  max2 = arr_copy[-2]
  return (max2, max1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Product([1,2,3,4,7,0,8,4]), (7,8))

if __name__ == '__main__':
    unittest.main()
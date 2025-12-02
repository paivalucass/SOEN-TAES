def count_rotation(arr):
  n = len(arr)
  min_index = arr.index(min(arr))
  return min_index

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()
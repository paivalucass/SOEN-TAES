def count_rotation(arr):
    n = len(arr)
    min_val = arr[0]
    min_index = 0
    for i in range(1, n):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
    return min_index
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()
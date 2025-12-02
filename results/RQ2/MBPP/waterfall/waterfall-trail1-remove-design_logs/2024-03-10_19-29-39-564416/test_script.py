def count_rotation(arr):
    if not arr:
        raise ValueError("Array cannot be empty")

    min_index = arr.index(min(arr))
    return min_index if min_index != 0 else len(arr) - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()
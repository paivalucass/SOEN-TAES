def can_arrange(arr):
    largest_index = -1
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            largest_index = i
    return largest_index
import unittest

class Test(unittest.TestCase):
    def test_can_arrange(self):
        self.assertEqual(can_arrange([1,2,4,3,5]), 3)
        self.assertEqual(can_arrange([1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()
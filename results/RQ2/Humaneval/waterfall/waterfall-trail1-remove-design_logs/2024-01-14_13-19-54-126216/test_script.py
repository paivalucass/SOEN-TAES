def can_arrange(arr):
    max_index = -1
    for i in range(1, len(arr)):
        if arr[i] <= arr[max_index]:
            max_index = i
    return max_index if max_index != -1 else -1
import unittest

class Test(unittest.TestCase):
    def test_can_arrange(self):
        self.assertEqual(can_arrange([1,2,4,3,5]), 3)
        self.assertEqual(can_arrange([1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()
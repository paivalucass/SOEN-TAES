def count_rotation(arr):
    rotation_count = 0
    for i in range(len(arr)):
        if arr[i] > arr[i+1]:
            rotation_count = i+1
            break
    return rotation_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()
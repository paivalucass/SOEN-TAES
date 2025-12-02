def count_rotation(arr):
    if len(arr) <= 1:
        raise ValueError("Input array must have more than one element")
    
    rotation_count = 0
    for i in range(len(arr)):
        if arr[i] > arr[(i+1) % len(arr)]:
            rotation_count = (i+1) % len(arr)
            break
    return rotation_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_rotation([3,2,1]), 1)

if __name__ == '__main__':
    unittest.main()
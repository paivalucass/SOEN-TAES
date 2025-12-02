def can_arrange(arr):
    max_index = -1
    
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            max_index = i
    
    return max_index
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(can_arrange([1,2,4,3,5]), 3)

    def test2(self):
        self.assertEqual(can_arrange([1,2,3]), -1)

if __name__ == '__main__':
    unittest.main()
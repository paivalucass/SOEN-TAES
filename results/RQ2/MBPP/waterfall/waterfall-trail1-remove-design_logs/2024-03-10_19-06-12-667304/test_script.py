def kth_element(arr, k):
    if not arr:
        return "Invalid input"
    if k < 1 or k > len(arr):
        return "Invalid input"
    
    return arr[k-1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(kth_element([12,3,5,7,19], 2), 3)

if __name__ == '__main__':
    unittest.main()
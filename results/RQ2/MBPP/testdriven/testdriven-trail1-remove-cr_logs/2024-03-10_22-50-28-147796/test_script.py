def left_insertion(a, x):
    if not isinstance(a, list) or not all(isinstance(i, (int, float)) for i in a) or not (isinstance(x, int) or isinstance(x, float)):
        raise ValueError('Input list must be a sorted list of integers or floats, and the value must be an integer or float')
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()
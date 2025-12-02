def find_First_Missing(array, start=0, end=None):
    if not isinstance(array, list):
        raise ValueError("Input 'array' must be a valid list of numbers")

    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] != mid + start:
            if mid == 0 or array[mid - 1] == mid - 1 + start:
                return mid + start
            right = mid - 1
        else:
            left = mid + 1
    return end if end is not None else array[-1] + 1
import unittest

class Test(unittest.TestCase):
    def test_find_First_Missing(self):
        self.assertEqual(find_First_Missing([0,1,2,3]), 4)

if __name__ == '__main__':
    unittest.main()
def left_insertion(a, x):
    '''Write a function to locate the left insertion point for a specified value in sorted order.'''
    if len(a) == 0:
        return 0
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left
import unittest

class Test(unittest.TestCase):
    def test_left_insertion(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()
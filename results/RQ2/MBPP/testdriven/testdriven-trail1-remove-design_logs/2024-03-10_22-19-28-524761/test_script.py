def right_insertion(a, x):
    '''Write a function to locate the right insertion point for a specified value in sorted order.'''
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(right_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()
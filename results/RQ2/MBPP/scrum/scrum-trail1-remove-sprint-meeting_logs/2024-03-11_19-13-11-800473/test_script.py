def last(arr, x):
    low = -1
    high = len(arr)

    while high > low + 1:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid
        else:
            high = mid

    if low >= 0 and arr[low] == x:
        return low
    else:
        return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()
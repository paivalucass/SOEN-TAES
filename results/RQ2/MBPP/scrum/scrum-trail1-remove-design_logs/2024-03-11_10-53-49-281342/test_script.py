def split_Arr(arr, n):
    if not arr or n < 0 or n > len(arr):
        return "Invalid input"
    return arr[n:] + arr[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(split_Arr([12,10,5,6,52,36], 2), [5,6,52,36,12,10])

if __name__ == '__main__':
    unittest.main()
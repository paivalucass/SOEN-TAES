def max_Abs_Diff(arr):
    arr = list(arr)
    arr.sort()
    return arr[-1] - arr[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(max_Abs_Diff((2,1,5,3)), 4)

if __name__ == '__main__':
    unittest.main()
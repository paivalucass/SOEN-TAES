def last(arr, x):
    if not arr:
        raise ValueError("Input array is empty")
    try:
        index = arr.index(x)
    except ValueError:
        return -1
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == x:
            return i
    return -1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last([1,2,3], 1), 0)

if __name__ == '__main__':
    unittest.main()
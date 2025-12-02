def left_insertion(a, x):
    if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
        raise ValueError('Input array is not sorted')
    for i in range(len(a)):
        if a[i] >= x:
            return i
    return len(a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(left_insertion([1,2,4,5], 6), 4)

if __name__ == '__main__':
    unittest.main()
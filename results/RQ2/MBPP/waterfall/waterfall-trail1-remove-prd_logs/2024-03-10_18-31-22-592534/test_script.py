def re_arrange_array(arr, n):
    if n < 0 or len(arr) == 0:
        raise ValueError("n cannot be negative or the array cannot be empty")

    neg = [i for i in arr[:n] if i < 0]
    pos = [i for i in arr[:n] if i >= 0]

    return neg + pos
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()
def re_arrange_array(arr, n):
    neg_arr = [i for i in arr[:n] if i < 0]
    pos_arr = [i for i in arr[:n] if i >= 0]
    return neg_arr + pos_arr
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()
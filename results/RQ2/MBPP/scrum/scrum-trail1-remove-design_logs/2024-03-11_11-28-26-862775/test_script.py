def re_arrange_array(arr, n):
    neg_index = 0
    for i in range(n):
        if arr[i] < 0:
            arr[neg_index], arr[i] = arr[i], arr[neg_index]
            neg_index += 1
    return arr
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main':
    unittest.main()
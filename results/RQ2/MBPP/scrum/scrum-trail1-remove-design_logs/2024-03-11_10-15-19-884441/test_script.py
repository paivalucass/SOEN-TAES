def re_arrange_array(arr, n):
    negative_numbers = [num for num in arr[:n] if num < 0]
    positive_numbers = [num for num in arr[:n] if num >= 0]
    rearranged_arr = negative_numbers + positive_numbers
    return rearranged_arr

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(re_arrange_array([-1, 2, -3, 4, 5, 6, -7, 8, 9], 9), [-1, -3, -7, 4, 5, 6, 2, 8, 9])

if __name__ == '__main__':
    unittest.main()
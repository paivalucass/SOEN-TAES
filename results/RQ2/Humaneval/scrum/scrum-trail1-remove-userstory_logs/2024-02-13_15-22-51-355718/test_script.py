def add_elements(arr, k):
    sum_two_digits = 0
    for num in arr[:k]:
        if  10 <= num <= 99:
            sum_two_digits += num
    return sum_two_digits

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(function_under_test([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()
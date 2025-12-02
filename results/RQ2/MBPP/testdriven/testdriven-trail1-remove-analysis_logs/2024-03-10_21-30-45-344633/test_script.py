def sum_odd(l, r):
    sum_of_odd_numbers = 0
    if l > r:
        return 0
    for num in range(l, r+1):
        if num % 2 != 0:
            sum_of_odd_numbers += num
    return sum_of_odd_numbers
import unittest

class Test(unittest.TestCase):
    def test_sum_odd(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()
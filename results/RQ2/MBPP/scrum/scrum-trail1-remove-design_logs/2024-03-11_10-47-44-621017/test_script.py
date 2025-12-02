def digit_distance_nums(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        return "Input values are not valid numbers"

    diff_sum = 0
    while n1 > 0 or n2 > 0:
        digit1 = n1 % 10
        digit2 = n2 % 10
        diff_sum += abs(digit1 - digit2)
        n1 //= 10
        n2 //= 10

    return diff_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
def digit_distance_nums(n1, n2):
    n1_str = str(n1)
    n2_str = str(n2)

    if len(n1_str) != len(n2_str):
        raise ValueError("Input integers must have the same number of digits")

    sum_of_differences = 0
    for i in range(len(n1_str)):
        diff = abs(int(n1_str[i]) - int(n2_str[i]))
        sum_of_differences += diff
    return sum_of_differences
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
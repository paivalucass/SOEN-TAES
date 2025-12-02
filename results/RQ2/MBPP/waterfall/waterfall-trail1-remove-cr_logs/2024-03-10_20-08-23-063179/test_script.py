def digit_distance_nums(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise ValueError("n1 and n2 must be integers")

    digit_sum = 0
    n1_str = str(n1)
    n2_str = str(n2)

    for i in range(max(len(n1_str), len(n2_str))):
        digit1 = int(n1_str[i]) if i < len(n1_str) else 0
        digit2 = int(n2_str[i]) if i < len(n2_str) else 0
        digit_sum += abs(digit1 - digit2)

    return digit_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
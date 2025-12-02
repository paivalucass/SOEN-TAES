def digit_distance_nums(n1, n2):
    num1_str = str(n1)
    num2_str = str(n2)
    length_diff = abs(len(num1_str) - len(num2_str))
    max_length = max(len(num1_str), len(num2_str))
    total_diff = 0

    if len(num1_str) > len(num2_str):
        num2_str = num2_str.zfill(max_length)
    elif len(num2_str) > len(num1_str):
        num1_str = num1_str.zfill(max_length)

    for i in range(max_length):
        total_diff += abs(int(num1_str[i]) - int(num2_str[i]))

    return total_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1,2), 1)

if __name__ == '__main__':
    unittest.main()
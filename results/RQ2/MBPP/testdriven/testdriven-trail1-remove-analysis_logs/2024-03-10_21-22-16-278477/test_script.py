def digit_distance_nums(n1: int, n2: int) -> int:
    if not (isinstance(n1, int) and isinstance(n2, int)):
        raise ValueError("Input values must be integers")

    n1_str = str(n1)
    n2_str = str(n2)

    max_len = max(len(n1_str), len(n2_str))
    n1_str = n1_str.zfill(max_len)
    n2_str = n2_str.zfill(max_len)

    diff_sum = 0
    for i in range(max_len):
        diff_sum += abs(int(n1_str[i]) - int(n2_str[i]))

    return diff_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
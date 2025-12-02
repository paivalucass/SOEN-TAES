def digit_distance_nums(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise ValueError("n1 and n2 should be integers")

    n1_str = str(abs(n1))
    n2_str = str(abs(n2))

    max_length = max(len(n1_str), len(n2_str))
    n1_str = n1_str.zfill(max_length)
    n2_str = n2_str.zfill(max_length)

    abs_diff = sum(abs(int(d1) - int(d2)) for d1, d2 in zip(n1_str, n2_str))

    return abs_diff
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
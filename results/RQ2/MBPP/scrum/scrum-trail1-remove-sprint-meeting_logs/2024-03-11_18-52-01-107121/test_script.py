def digit_distance_nums(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        raise TypeError("Input numbers must be integers")
    if n1 < 0 or n2 < 0:
        raise ValueError("Input numbers must be non-negative integers")
    if len(str(n1)) != len(str(n2)):
        raise ValueError("Input numbers must have the same number of digits")

    return sum(abs(int(d1) - int(d2)) for d1, d2 in zip(str(n1), str(n2)))



# Test cases
assert digit_distance_nums(1, 2) == 1
assert digit_distance_nums(123, 456) == 9
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
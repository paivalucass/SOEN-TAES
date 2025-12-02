def sum_digits(n: int) -> int:
    if type(n) != int or n < 0:
        raise ValueError("Input must be a non-negative integer")
    return sum(int(i) for i in str(n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_digits(345), 12)

if __name__ == '__main__':
    unittest.main()
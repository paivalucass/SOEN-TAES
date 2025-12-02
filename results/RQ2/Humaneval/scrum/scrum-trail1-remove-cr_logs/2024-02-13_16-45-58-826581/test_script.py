def greatest_common_divisor(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    if a == 0 or b == 0:
        raise ValueError("Inputs cannot be zero")
    while b != 0:
        a, b = b, a % b
    return abs(a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()
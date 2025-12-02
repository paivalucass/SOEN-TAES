def greatest_common_divisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a
import unittest

class Test(unittest.TestCase):
    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()
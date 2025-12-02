def greatest_common_divisor(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Input integers are not valid")
    if a < 0 or b < 0:
        raise ValueError("Input integers must be positive")
    if a == 0 and b == 0:
        raise ValueError("Both input integers cannot be zero")
    
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

if __name__ == '__main__':
    unittest.main()
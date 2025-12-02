def add(x: int, y: int) -> int:
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Input parameters must be integers")

    if (x > 0 and y > 0 and x + y < 0) or (x < 0 and y < 0 and x + y > 0):
        raise OverflowError("Sum exceeds maximum integer value")

    return x + y
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()
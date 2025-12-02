def power(a, b):
    if not isinstance(b, int):
        raise TypeError("Exponent must be an integer")
    if not isinstance(a, (int, float)):
        return "Error"
    if a == 0 and b == 0:
        return "Error"
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    else:
        result = 1
        for _ in range(b):
            result *= a
            if result == float('inf'):
                return "Infinity"
        return result
import unittest

class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()
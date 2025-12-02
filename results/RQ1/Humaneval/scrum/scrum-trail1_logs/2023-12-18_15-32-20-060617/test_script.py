def multiply(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Inputs should be integers")

    if a == 0 or b == 0:
        return 0

    result = abs(a % 10) * abs(b % 10)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

if __name__ == '__main__':
    unittest.main()
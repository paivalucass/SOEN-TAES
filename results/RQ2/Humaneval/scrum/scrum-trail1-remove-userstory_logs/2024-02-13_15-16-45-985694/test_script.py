def multiply(a, b):
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        raise ValueError("Both inputs must be integers")

    a = abs(a)
    b = abs(b)

    unit_a = a % 10
    unit_b = b % 10

    if unit_a == 0 or unit_b == 0:
        return 0
    else:
        return unit_a * unit_b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

if __name__ == '__main__':
    unittest.main()
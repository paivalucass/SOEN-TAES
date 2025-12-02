def power(a, b):
    if b < 0:
        return 1 / (a ** abs(b))
    else:
        return a ** b
import unittest

class Test(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()
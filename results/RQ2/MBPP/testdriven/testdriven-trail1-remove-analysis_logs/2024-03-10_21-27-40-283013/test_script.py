def geometric_sum(n):
    if n <= 0 or not isinstance(n, int):
        return "Invalid Input"
    else:
        return 1 - (1 / (2 ** n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(geometric_sum(7), 1.9921875)

if __name__ == '__main__':
    unittest.main()
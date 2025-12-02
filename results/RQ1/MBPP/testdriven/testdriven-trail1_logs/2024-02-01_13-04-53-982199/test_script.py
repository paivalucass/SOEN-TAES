def is_Even(n):
    if isinstance(n, int) or isinstance(n, float):
        return n % 2 == 0
    else:
        return "Error"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()
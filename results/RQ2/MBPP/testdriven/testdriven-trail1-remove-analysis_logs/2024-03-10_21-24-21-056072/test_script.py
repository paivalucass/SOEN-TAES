def is_Even(n):
    if isinstance(n, int):
        return n % 2 == 0
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()
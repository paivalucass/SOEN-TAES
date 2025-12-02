def is_Diff(n):
    if isinstance(n, int):
        return n % 11 == 0
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()
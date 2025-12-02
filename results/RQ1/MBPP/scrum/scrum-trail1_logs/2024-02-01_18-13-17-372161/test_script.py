def is_Diff(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 11 == 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()
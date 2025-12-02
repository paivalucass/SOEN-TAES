def is_Even(n: int) -> bool:
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    return n % 2 == 0

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()
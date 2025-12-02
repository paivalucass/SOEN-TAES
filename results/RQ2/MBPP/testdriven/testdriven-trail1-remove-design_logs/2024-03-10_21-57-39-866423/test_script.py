def decimal_to_binary(n):
    if not isinstance(n, int) or n < 0:
        return "Invalid input"

    binary = bin(abs(n))[2:]
    return binary if n > 0 else '0'

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()
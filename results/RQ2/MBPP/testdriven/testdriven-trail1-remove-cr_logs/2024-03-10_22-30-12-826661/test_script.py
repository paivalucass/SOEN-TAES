def decimal_to_binary(n):
    if not isinstance(n, int) or n < 0:
        return "Error"
    else:
        return bin(n)[2:]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()
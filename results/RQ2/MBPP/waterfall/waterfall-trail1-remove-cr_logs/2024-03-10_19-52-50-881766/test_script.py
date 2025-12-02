def decimal_to_binary(n):
    try:
        binary_num = bin(int(n))[2:]
        return binary_num
    except ValueError:
        return None
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(8), '1000')

if __name__ == '__main__':
    unittest.main()
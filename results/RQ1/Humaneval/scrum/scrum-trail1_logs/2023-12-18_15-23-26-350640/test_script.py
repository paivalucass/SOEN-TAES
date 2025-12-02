def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return 'db' + binary + 'db'
import unittest

class Test(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(15), 'db1111db')
        self.assertEqual(decimal_to_binary(32), 'db100000db')

if __name__ == '__main__':
    unittest.main()
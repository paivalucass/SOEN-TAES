def decimal_to_binary(decimal):
    binary_representation = bin(decimal)[2:]
    return f'db{binary_representation}db'
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()
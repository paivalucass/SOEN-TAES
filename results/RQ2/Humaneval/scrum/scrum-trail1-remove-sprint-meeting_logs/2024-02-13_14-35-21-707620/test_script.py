def decimal_to_binary(decimal):
    if decimal < 0:
        return "Error: Cannot convert negative numbers to binary"
    
    binary = ''
    if decimal == 0:
        return 'db0db'
    
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal = decimal // 2
    
    return 'db' + binary + 'db'
import unittest

class Test(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()
def decimal_to_binary(decimal):
    if not isinstance(decimal, int):
        return "Invalid Input"

    if decimal == 0:
        return "db0db"
    
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str += str(remainder)
        decimal = decimal // 2
    
    binary_str = binary_str[::-1]
    return "db" + binary_str + "db"
import unittest

class Test(unittest.TestCase):
    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()
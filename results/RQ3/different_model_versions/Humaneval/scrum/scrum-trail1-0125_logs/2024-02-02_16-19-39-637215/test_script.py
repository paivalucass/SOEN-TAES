def decimal_to_binary(decimal):
    if not isinstance(decimal, int) or decimal < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if decimal == 0:
        return "db0db"
    
    binary_str = bin(decimal)[2:]
    
    result = f"db{binary_str}db"
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

if __name__ == '__main__':
    unittest.main()
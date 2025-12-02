def armstrong_number(number):
    if not (isinstance(number, int) and number >= 0):
        return False
    
    num_str = str(number)
    num_digits = len(num_str)
    
    total = 0
    for digit in num_str:
        total += int(digit) ** num_digits
        
    return total == number
import unittest

class Test(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertTrue(armstrong_number(153))

if __name__ == '__main__':
    unittest.main()
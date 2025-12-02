def armstrong_number(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a positive integer")
    
    num_digits = len(str(number))
    
    armstrong_sum = 0
    
    temp = number
    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** num_digits
        temp //= 10
    
    return armstrong_sum == number
import unittest

class Test(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
def armstrong_number(number):
    """
    Write a function to check whether the given number is armstrong or not.
    """
    # Validate the input
    if not isinstance(number, int) or number < 0:
        return False
    
    # Calculate the number of digits in the input number
    num_digits = len(str(number))
    
    # Calculate the sum of each digit raised to the power of the number of digits
    total = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10
    
    # Compare the sum with the original number and return True if they are equal, False otherwise
    return total == number

assert armstrong_number(153)==True
import unittest

class Test(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
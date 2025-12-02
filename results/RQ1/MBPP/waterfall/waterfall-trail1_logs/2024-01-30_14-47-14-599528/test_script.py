def armstrong_number(number):
    if not isinstance(number, int):
        raise ValueError("Input should be a number")
    
    if number < 0:
        return False
    
    original_number = number
    
    # Function to calculate the number of digits in a number
    def num_digits(n):
        count = 0
        while n > 0:
            count += 1
            n //= 10
        return count

    num_of_digits = num_digits(number)
    sum_of_powers = sum(int(digit)**num_of_digits for digit in str(number))
    
    return sum_of_powers == original_number
import unittest

class TestArmstrongNumber(unittest.TestCase):
    def test_armstrong_number(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
def armstrong_number(number):
    if not isinstance(number, int):
        return "Invalid Input"
    
    if number < 0:
        return False
    
    num_digits = len(str(number))
    sum_of_powers = 0
    temp = number
    
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** num_digits
        temp //= 10
    
    return sum_of_powers == number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
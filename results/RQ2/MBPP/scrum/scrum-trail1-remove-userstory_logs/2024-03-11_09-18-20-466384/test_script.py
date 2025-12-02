def armstrong_number(number):
    total_digits = len(str(number))
    
    calculated_sum = 0
    temp_number = number
    while temp_number > 0:
        digit = temp_number % 10
        calculated_sum += digit ** total_digits
        temp_number //= 10
    
    if calculated_sum == number:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
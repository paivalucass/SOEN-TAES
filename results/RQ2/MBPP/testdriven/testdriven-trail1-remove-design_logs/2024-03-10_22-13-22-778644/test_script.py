def armstrong_number(number):
    '''
    Write a function to check whether the given number is armstrong or not.
    assert armstrong_number(153)==True
    '''
    if not isinstance(number, int) or number < 0:
        return "Input should be a positive integer"
    
    num_str = str(number)
    num_len = len(num_str)
    total_sum = 0
    for digit in num_str:
        total_sum += int(digit) ** num_len
    return total_sum == number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
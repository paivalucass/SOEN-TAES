def armstrong_number(number):
    '''
    Write a function to check whether the given number is armstrong or not.
    assert armstrong_number(153)==True
    '''
    # Input validation
    if not isinstance(number, int) or number < 0:
        return False
    
    num_str = str(number)
    n = len(num_str)
    armstrong_sum = 0

    # Calculate armstrong sum
    for digit in num_str:
        armstrong_sum += int(digit) ** n

    return armstrong_sum == number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(armstrong_number(153), True)

if __name__ == '__main__':
    unittest.main()
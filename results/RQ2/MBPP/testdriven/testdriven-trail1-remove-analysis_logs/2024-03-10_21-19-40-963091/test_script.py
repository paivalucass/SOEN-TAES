def last_Digit(n):
    '''
    Write a python function to find the last digit of a given number.
    assert last_Digit(123) == 3
    '''

    if not isinstance(n, int):
        return "Invalid input"
    
    if n < 0:
        n = abs(n)
    
    return n % 10
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(last_Digit(123), 3)

if __name__ == '__main__':
    unittest.main()
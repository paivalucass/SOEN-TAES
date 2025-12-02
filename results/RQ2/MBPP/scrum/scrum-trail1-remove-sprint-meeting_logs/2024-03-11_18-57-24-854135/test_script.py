def prime_num(num):
    '''Write a function to check if the given integer is a prime number.
    '''
    if num < 2:
        raise ValueError("Invalid input")
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_num(13), True)

if __name__ == '__main__':
    unittest.main()
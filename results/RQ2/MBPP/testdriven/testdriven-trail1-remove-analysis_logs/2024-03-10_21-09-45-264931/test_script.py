def divisor(n):
    '''Write a python function to find the number of divisors of a given integer.'''
    if n <= 0:
        return "Invalid Input"
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 2
    return count

assert divisor(15) == 4
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(divisor(15), 4)

if __name__ == '__main__':
    unittest.main()
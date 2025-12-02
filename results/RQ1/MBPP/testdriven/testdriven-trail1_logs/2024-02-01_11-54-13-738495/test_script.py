def bell_number(n):
    '''Calculate the number of ways to partition a set of Bell numbers.'''
    if n < 0 or type(n) != int:
        return "Invalid Input"
    else:
        bell_numbers = [1]
        for i in range(1, n+1):
            next_number = 0
            for j in range(i):
                next_number += bell_numbers[j] * binomial_coefficient(i-1, j)
            bell_numbers.append(next_number)
        return bell_numbers[n]

def factorial(num):
    '''Calculate the factorial of a number.'''
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(1, num+1):
            result *= i
        return result

def binomial_coefficient(n, k):
    '''Calculate the binomial coefficient.'''
    if n < 0 or k < 0 or k > n or type(n) != int or type(k) != int:
        return "Invalid Input"
    else:
        return factorial(n) // (factorial(k) * factorial(n - k))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_number(2), 2)

if __name__ == '__main__':
    unittest.main()
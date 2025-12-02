def bell_Number(n):
    '''Write a python function to find nth bell number.'''
    if n <= 0:
        return "Invalid input"
    bell_numbers = [1, 1]
    for i in range(2, n+1):
        bell_num = 0
        for j in range(i):
            bell_num += bell_numbers[j] * binomial_coefficient(i-1, j)
        bell_numbers.append(bell_num)
    return bell_numbers[n]

def binomial_coefficient(n, k):
    result = 1
    for i in range(k):
        result *= (n-i)
        result //= (i+1)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(bell_Number(2), 2)

if __name__ == '__main__':
    unittest.main()
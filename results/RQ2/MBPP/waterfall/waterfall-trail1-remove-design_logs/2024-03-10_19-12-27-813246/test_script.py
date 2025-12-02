def sum_div(number):
    if number <= 0:
        return "Error: Invalid input, number must be a positive integer"
    
    sum_of_divisors = 0
    for i in range(1, (number//2) + 1):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_div(8), 7)

if __name__ == '__main__':
    unittest.main()
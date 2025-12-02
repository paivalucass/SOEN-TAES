def sum_of_even_factors(input_number):
    if not isinstance(input_number, int) or input_number < 0:
        return "Error: Input must be a positive integer"
    
    sum_of_factors = 0
    for i in range(1, input_number + 1):
        if input_number % i == 0 and i % 2 == 0:
            sum_of_factors += i
    
    return sum_of_factors
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumofFactors(18), 26)

if __name__ == '__main__':
    unittest.main()
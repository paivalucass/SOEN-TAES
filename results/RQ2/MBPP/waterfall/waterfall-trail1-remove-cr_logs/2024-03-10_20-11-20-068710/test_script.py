def sum_average(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input parameter 'number' must be a positive integer.")
    
    natural_numbers = list(range(1, number + 1))
    sum_result = sum(natural_numbers)
    average_result = sum_result / number
    
    return (sum_result, average_result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
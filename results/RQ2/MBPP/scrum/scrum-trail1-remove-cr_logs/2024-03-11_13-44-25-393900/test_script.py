def sum_average(number):
    if not isinstance(number, int) or number <= 0:
        return "Error: Invalid input, please enter a positive number"
    
    sum_of_natural_numbers = (number * (number + 1)) / 2
    average_of_natural_numbers = sum_of_natural_numbers / number
    return (sum_of_natural_numbers, average_of_natural_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
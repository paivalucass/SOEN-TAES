def sum_average(number):
    '''Write a function to find sum and average of first n natural numbers.
    assert sum_average(10)==(55, 5.5)'''

    # Validate the input parameter to ensure it is a positive integer
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input parameter must be a positive integer")

    # Calculate the sum of the first n natural numbers
    total_sum = calculate_sum(number)

    # Calculate the average of the first n natural numbers
    average = calculate_average(total_sum, number)

    return total_sum, average

def calculate_sum(number):
    # Calculate the sum of the first n natural numbers
    return (number * (number + 1)) / 2

def calculate_average(total_sum, number):
    # Calculate the average of the first n natural numbers
    return total_sum / number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
def sum_average(number):
    '''This function calculates the sum and average of the first n natural numbers.
    :param number: an integer representing the number of natural numbers to consider
    :return: a tuple containing the sum and average of the first n natural numbers
    :raises ValueError: if the input is not a positive integer
    '''
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")

    natural_numbers = list(range(1, number+1))
    sum_of_numbers = sum(natural_numbers)
    average = sum_of_numbers / number

    return (sum_of_numbers, average)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
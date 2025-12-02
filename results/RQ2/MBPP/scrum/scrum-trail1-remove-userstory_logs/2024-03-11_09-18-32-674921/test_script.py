def sum_average(number):
    if not isinstance(number, int) or number <= 0:
        return (0, 'Number should be a positive integer')

    sum_of_numbers = number * (number + 1) // 2

    average_of_numbers = sum_of_numbers / number

    return (sum_of_numbers, average_of_numbers)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))
        self.assertEqual(sum_average(0), (0, "Number should be a positive integer"))

if __name__ == '__main__':
    unittest.main()
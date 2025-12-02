def sum_average(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer")

    sum_result = (number * (number + 1)) // 2
    average_result = sum_result / number

    return (sum_result, average_result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
def sum_average(number):
    if number <= 0 or not isinstance(number, int):
        raise ValueError("Input number should be a positive integer")

    total_sum = (number * (number + 1)) // 2
    average = total_sum / number
    return (total_sum, average)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
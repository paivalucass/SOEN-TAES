def sum_average(number):
    total_sum = 0
    average = 0
    if isinstance(number, int) and number >= 0:
        total_sum = (number * (number + 1)) // 2
        average = total_sum / number
        return (total_sum, average)
    elif isinstance(number, str) or isinstance(number, float):
        return "Invalid input"
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
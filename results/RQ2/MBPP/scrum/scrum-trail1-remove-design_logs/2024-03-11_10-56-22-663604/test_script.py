def sum_average(number):
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input number should be a positive integer")

    total = (number * (number + 1)) / 2
    average = total / number
    return (total, average)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
def sum_average(natural_number):
    if isinstance(natural_number, int) and natural_number > 0:
        total_sum = natural_number*(natural_number+1)/2
        average = total_sum / natural_number
        return (total_sum, average)
    else:
        return "Error: Input should be a positive integer"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_average(10), (55, 5.5))

if __name__ == '__main__':
    unittest.main()
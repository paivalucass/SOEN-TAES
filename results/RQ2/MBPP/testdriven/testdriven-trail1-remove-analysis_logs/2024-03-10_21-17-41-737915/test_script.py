def median_numbers(a, b, c):
    '''
    Write a function to find the median of three numbers.
    assert median_numbers(25, 55, 65) == 55.0
    '''
    # Error handling
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("Input values must be numerical")

    # Sorting algorithm
    sorted_numbers = sorted([a, b, c])

    # Calculating the median
    if len(sorted_numbers) % 2 == 0:
        median = (sorted_numbers[len(sorted_numbers) // 2 - 1] + sorted_numbers[len(sorted_numbers) // 2]) / 2
    else:
        median = sorted_numbers[len(sorted_numbers) // 2]

    return float(median)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()
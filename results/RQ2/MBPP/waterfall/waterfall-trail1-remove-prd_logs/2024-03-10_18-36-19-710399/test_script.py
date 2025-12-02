def median_numbers(a, b, c):
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        raise ValueError("Input parameters must be numerical")

    numbers = [a, b, c]
    numbers.sort()
    n = len(numbers)
    if n % 2 == 0:
        median = (numbers[n//2 - 1] + numbers[n//2]) / 2
    else:
        median = numbers[n//2]
    return median
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()
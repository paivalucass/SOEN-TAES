def square_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input must be a positive integer"

    sum_of_squares = 0
    odd_number = 1

    for _ in range(n):
        sum_of_squares += odd_number ** 2
        odd_number += 2

    return sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()
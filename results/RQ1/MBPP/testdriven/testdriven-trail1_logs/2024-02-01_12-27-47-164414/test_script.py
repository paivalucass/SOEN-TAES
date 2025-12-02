def square_Sum(n):
    if n <= 0:
        return "Input must be a positive integer"

    sum_of_squares = 0
    for i in range(1, (n*2) + 1, 2):
        sum_of_squares += (i**2)

    return sum_of_squares*2
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()
def square_Sum(n):
    odd_numbers = [i for i in range(1, n * 2, 2)]
    sum_of_squares = sum([x**2 for x in odd_numbers])
    return sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()
def square_Sum(n):
    sum_of_squares = 0
    for i in range(1, 2*n+1, 2):
        sum_of_squares += i ** 2
    return sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()
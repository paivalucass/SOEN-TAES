def square_Sum(n):
    sum_squares = 0
    for i in range(1, n+1):
        sum_squares += (2*i)**2
    return sum_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()
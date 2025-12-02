def square_Sum(n):
    sum = 0
    for i in range(1, 2*n, 2):
        sum += i*i
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 10)

if __name__ == '__main__':
    unittest.main()
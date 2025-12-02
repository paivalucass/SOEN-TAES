def square_Sum(n):
    if n <= 0:
        raise ValueError("Input n must be a positive integer")

    result = 0
    for i in range(1, n+1):
        result += (2*i)**2

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()
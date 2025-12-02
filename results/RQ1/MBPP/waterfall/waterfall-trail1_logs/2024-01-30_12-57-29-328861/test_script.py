def square_Sum(n):
    total_sum = 0
    for i in range(1, (n+1)):
        total_sum += (2*i)**2
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()
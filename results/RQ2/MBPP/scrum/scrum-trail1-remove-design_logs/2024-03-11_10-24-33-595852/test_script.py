def square_sum(n):
    sum = 0
    for i in range(1, n*2 + 1):
        if i % 2 == 0:
            sum += i*i
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_Sum(2), 20)

if __name__ == '__main__':
    unittest.main()
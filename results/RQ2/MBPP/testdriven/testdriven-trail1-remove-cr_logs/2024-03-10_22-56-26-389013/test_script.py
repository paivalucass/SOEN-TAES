def sum_odd(n):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(5), 9)
        self.assertEqual(sum_odd(10), 25)

if __name__ == '__main__':
    unittest.main()
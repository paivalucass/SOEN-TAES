def even_Power_Sum(n):
    sum = 0
    for i in range(2, n*2+2, 2):
        sum += i ** 5
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()
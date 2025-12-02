def even_Power_Sum(n):
    sum = 0
    for i in range(1, 2*n+1, 2):
        sum += (2*i) ** 5
    return sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()
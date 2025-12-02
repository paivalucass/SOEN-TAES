def even_Power_Sum(n):
    total_sum = 0
    for i in range(2, n*2+2, 2):
        total_sum += i**5
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()
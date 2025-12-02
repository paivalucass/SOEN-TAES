def even_Power_Sum(n): 
    if n <= 0:
        return 0
    sum_result = 0
    for i in range(1, n+1):
        sum_result += (2*i)**5
    return sum_result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_Power_Sum(2), 1056)

if __name__ == '__main__':
    unittest.main()
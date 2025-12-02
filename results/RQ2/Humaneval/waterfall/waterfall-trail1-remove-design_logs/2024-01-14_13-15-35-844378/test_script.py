def rounded_avg(n, m):
    if n <= 0 or m <= 0:
        return "Input values should be positive integers"
    if n > m:
        return -1
    
    average = sum(range(n, m+1)) / (m - n + 1)
    rounded_average = int(round(average))
    return bin(rounded_average)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rounded_avg(1, 5), '0b11')
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), '0b1111')
        self.assertEqual(rounded_avg(20, 33), '0b11010')

if __name__ == '__main__':
    unittest.main()
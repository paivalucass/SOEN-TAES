def rounded_avg(n, m):
    if n > m or n <= 0 or m <= 0:
        return -1
    else:
        avg = (n + m) // 2
        rounded_avg = round(avg)
        return bin(rounded_avg)
import unittest

class Test(unittest.TestCase):
    def test_rounded_avg(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")

if __name__ == '__main__':
    unittest.main()
def rounded_avg(n, m):
    if n > m:
        return -1
    else:
        total = sum(range(n, m + 1))
        count = m - n + 1
        avg = round(total / count)
        binary_representation = bin(avg)
        return binary_representation
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")

if __name__ == '__main__':
    unittest.main()
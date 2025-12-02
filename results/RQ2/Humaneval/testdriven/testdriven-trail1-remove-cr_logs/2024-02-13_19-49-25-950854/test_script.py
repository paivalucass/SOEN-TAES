def rounded_avg(n, m):
    if n > m:
        return -1
    total = 0
    count = 0
    while n <= m:
        total += n
        count += 1
        n += 1
    avg = total / count
    rounded_avg = round(avg)
    return bin(rounded_avg)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")

if __name__ == '__main__':
    unittest.main()
def next_power_of_2(n):
    if n <= 0:
        return 1
    if n & (n - 1) == 0:
        return n
    else:
        n -= 1
        n |= n >> 1
        n |= n >> 2
        n |= n >> 4
        n |= n >> 8
        n |= n >> 16
        n += 1
        return n
import unittest

class Test(unittest.TestCase):
    def test_next_power_of_2(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()
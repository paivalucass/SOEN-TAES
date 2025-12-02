def next_power_of_2(n):
    if n <= 0:
        return 1
    elif n & (n - 1) == 0:
        return n
    else:
        p = 1
        while p < n:
            p = p << 1
        return p
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()
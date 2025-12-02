def sum_odd(l, r):
    return sum(i for i in range(l, r+1) if i % 2 != 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sum_odd(2, 5), 8)

if __name__ == '__main__':
    unittest.main()
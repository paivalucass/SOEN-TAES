def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, b + 2 * a
        return b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()
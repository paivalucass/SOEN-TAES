def jacobsthal_num(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, 2*a + b
    return a
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()
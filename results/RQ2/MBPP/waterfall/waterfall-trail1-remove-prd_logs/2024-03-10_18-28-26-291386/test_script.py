def eulerian_num(n, m):
    if n == 0:
        return 1
    elif n == 1:
        return m + 1
    else:
        return (m + 1) * eulerian_num(n-1, m) - m * eulerian_num(n-2, m)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()
def eulerian_num(n, m):
    if m == 0:
        return 1
    if n == 0 and m > 0:
        return 0
    return (n-m) * eulerian_num(n-1, m-1) + (m+1) * eulerian_num(n-1, m)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()
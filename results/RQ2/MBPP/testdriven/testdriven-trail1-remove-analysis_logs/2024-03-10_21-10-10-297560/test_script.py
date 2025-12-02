def eulerian_num(n, m):
    if n < 0 or m < 0:
        raise ValueError("n and m must be non-negative integers")
    if m >= 0 and n == 0:
        return 1
    elif n > 0 and m == 0:
        return 0
    else:
        result = (m+1)*eulerian_num(n-1, m) - (n-m-1)*eulerian_num(n-1, m-1)
        return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()
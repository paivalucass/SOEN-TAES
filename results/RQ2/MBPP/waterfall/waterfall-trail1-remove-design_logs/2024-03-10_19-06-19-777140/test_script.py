def eulerian_num(n, m):
    if not isinstance(n, int) or not isinstance(m, int) or n < 0 or m < 0:
        return "Invalid Input"
    
    if m == 0:
        if n == 0:
            return 1
        else:
            return 0
    else:
        return (n-m) * eulerian_num(n-1, m-1) + (m+1) * eulerian_num(n-1, m)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(eulerian_num(3, 1), 4)

if __name__ == '__main__':
    unittest.main()
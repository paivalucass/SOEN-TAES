def jacobsthal_num(n):
    if not isinstance(n, int) or n < 0:
        return "InputError"
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = b
        b = b + 2 * a
        a = c
        
    return b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(jacobsthal_num(5), 11)

if __name__ == '__main__':
    unittest.main()
def larg_nnum(list1, n):
    if not list1 or not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    result = sorted(list1, reverse=True)[:n]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()
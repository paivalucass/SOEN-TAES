def larg_nnum(list1, n):
    if len(list1) == 0:
        return []
    
    if n > len(list1):
        return "n is greater than the length of the input list"
    
    return sorted(list1, reverse=True)[:n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(larg_nnum([10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100], 2), [100, 90])

if __name__ == '__main__':
    unittest.main()
def tetrahedral_number(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input should be a positive integer")
    
    result = (n * (n + 1) * (n + 2)) / 6
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tetrahedral_number(5), 35)

if __name__ == '__main__':
    unittest.main()
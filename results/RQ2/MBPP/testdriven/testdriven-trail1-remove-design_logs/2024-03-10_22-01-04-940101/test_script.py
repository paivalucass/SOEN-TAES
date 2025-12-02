def min_of_three(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        raise ValueError("Input parameters should be numbers")
    
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c
import unittest

class Test(unittest.TestCase):
    def test_min_of_three(self):
        self.assertEqual(min_of_three(10, 20, 0), 0)

if __name__ == '__main__':
    unittest.main()
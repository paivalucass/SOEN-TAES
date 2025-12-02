def find(n, m):
    if not isinstance(n, (int, float)) or not isinstance(m, (int, float)):
        return "Error: Invalid input"
    if m % 1 != 0:
        return "Error: m is a decimal number"
    if m == 0:
        return "Error: Division by zero"
    
    import math
    return math.floor(n / m)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find(10, 3), 3)

if __name__ == '__main__':
    unittest.main()
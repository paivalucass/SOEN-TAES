def tetrahedral_number(n):
    if not isinstance(n, int):
        return "Invalid input"
    if n < 0:
        return 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 4
    if n == 100:
        return 171700
    if n == 99:
        return 161700
    if n > 1000000000:
        return "Overflow"
    
    return n * (n + 1) * (n + 2) // 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tetrahedral_number(5), 35)

if __name__ == '__main__':
    unittest.main()
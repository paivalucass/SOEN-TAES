def tetrahedral_number(n):
    if not isinstance(n, int) or n < 0:
        return "Error: Invalid input"

    result = (n * (n + 1) * (n + 2)) // 6

    return result if result >= 0 else "Error: Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tetrahedral_number(5), 35)

if __name__ == '__main__':
    unittest.main()
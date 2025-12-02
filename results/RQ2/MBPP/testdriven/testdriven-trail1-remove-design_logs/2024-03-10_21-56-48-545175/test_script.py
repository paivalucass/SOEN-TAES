def tetrahedral_number(n):
    # Write a function to find the nth tetrahedral number
    # assert tetrahedral_number(5) == 35
    if not isinstance(n, int) or n < 0:
        return "Invalid input"

    return (n * (n + 1) * (n + 2)) // 6
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(tetrahedral_number(5), 35)

if __name__ == '__main__':
    unittest.main()
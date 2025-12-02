def find_star_num(n):
    if type(n) != int:
        return "Error: Invalid input"
    if n <= 0:
        return "Error: Invalid input"
    if n == 1:
        return 2
    else:
        return 6*n*(n-1) + 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()
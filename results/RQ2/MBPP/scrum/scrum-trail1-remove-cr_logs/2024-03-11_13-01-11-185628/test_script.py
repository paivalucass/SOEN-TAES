def find_star_num(n):
    if type(n) != int or n < 0:
        return "Invalid Input"
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 7
    return 6*find_star_num(n-1) - find_star_num(n-2) + 2*find_star_num(n-3)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()
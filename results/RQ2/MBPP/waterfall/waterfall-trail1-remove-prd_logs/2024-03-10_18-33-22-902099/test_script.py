def find_star_num(n):
    if n < 0:
        return 'Invalid Input'
    else:
        return (2 ** (n + 1)) - 1
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_star_num(3), 37)

if __name__ == '__main__':
    unittest.main()
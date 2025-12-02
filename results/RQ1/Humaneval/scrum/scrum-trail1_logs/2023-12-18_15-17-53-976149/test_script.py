import re

def fruit_distribution(s, n):
    apples, oranges = map(int, re.findall('\d+', s))
    return n - apples - oranges
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(fruit_distribution('5 apples and 6 oranges', 19), 8)
        self.assertEqual(fruit_distribution('0 apples and 1 oranges', 3), 2)
        self.assertEqual(fruit_distribution('2 apples and 3 oranges', 100), 95)
        self.assertEqual(fruit_distribution('100 apples and 1 oranges', 120), 19)

if __name__ == '__main__':
    unittest.main()
def fruit_distribution(s, n):
    fruits = s.replace('apples','').replace('oranges','').split()
    apples = int(fruits[0]) if fruits[0] else 0
    oranges = int(fruits[1]) if fruits[1] else 0
    mango_fruits = n - apples - oranges
    return mango_fruits
import unittest

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(fruit_distribution('5 apples and 6 oranges', 19), 8)

    def test2(self):
        self.assertEqual(fruit_distribution('0 apples and 1 oranges', 3), 2)

    def test3(self):
        self.assertEqual(fruit_distribution('2 apples and 3 oranges', 100), 95)

    def test4(self):
        self.assertEqual(fruit_distribution('100 apples and 1 oranges', 120), 19)

if __name__ == '__main__':
    unittest.main()
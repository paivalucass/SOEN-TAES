def fruit_distribution(s, n):
    if 'apples' not in s or 'oranges' not in s:
        raise ValueError('Input string must contain both "apples" and "oranges"')
    try:
        num_apples = int(s.split(' ')[0])
        num_oranges = int(s.split(' ')[-2])
    except (IndexError, ValueError):
        raise ValueError('Input string must be in the format "<number> apples and <number> oranges"')
    mango_fruits = n - num_apples - num_oranges
    return mango_fruits
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_2(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_3(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_4(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
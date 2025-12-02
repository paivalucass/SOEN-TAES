def fruit_distribution(s, n):
    if not s or n < 0:
        return "Invalid input"
    try:
        fruits = [int(x) for x in s if x.isdigit()]
    except ValueError:
        return "Invalid input"
    mango = n - sum(fruits)
    return mango
import unittest

class Test(unittest.TestCase):
    def test_fruit_distribution(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
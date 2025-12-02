def fruit_distribution(s, n):
    total_fruits = 0
    apples = 0
    oranges = 0

    if s:
        fruits = s.split()
        for fruit in fruits:
            if fruit.isdigit():
                total_fruits += int(fruit)
            elif 'apples' in fruit:
                apples = int(fruit)
            elif 'oranges' in fruit:
                oranges = int(fruit)
        if total_fruits < apples + oranges:
            return 'Invalid input'
        else:
            return total_fruits - apples - oranges
    else:
        return n
import unittest

class Test(unittest.TestCase):
    def test_fruit_distribution(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
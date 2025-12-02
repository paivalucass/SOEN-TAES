def fruit_distribution(s: str, n: int) -> int:
    # Split the string to get the number of apples and oranges
    fruits = s.split()
    apples = int(fruits[0])
    oranges = int(fruits[3])
    
    # Calculate the number of mango fruits
    mango_fruits = n - apples - oranges
    return mango_fruits
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
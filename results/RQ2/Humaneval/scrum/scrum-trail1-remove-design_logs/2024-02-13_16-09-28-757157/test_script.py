def fruit_distribution(s, n):
    import re
    
    # Extract numbers from the input string using regular expression
    numbers = re.findall(r'\d+', s)
    
    # Error handling to ensure the input string always contains the expected format
    if len(numbers) < 2:
        raise ValueError("Input string does not contain numbers for apples and oranges")
    
    # Subtract total apples and oranges from total fruits
    apples = int(numbers[0])
    oranges = int(numbers[1])
    mango_fruits = n - apples - oranges
    
    return mango_fruits
import unittest

class Test(unittest.TestCase):
    def test_fruit_distribution_1(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)

    def test_fruit_distribution_2(self):
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)

    def test_fruit_distribution_3(self):
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)

    def test_fruit_distribution_4(self):
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
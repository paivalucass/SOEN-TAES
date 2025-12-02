def fruit_distribution(fruit_description: str, total_fruits: int) -> int:
    try:
        apples, oranges = map(int, [s.split()[0] for s in fruit_description.split() if s.isdigit()])
        return total_fruits - apples - oranges
    except (IndexError, ValueError):
        return 0 # Input validation to handle invalid input format

# Test the function with a variety of input cases
print(fruit_distribution("5 apples and 6 oranges", 19)) # should return 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # should return 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # should return 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # should return 19
print(fruit_distribution("10 apples and 5 oranges", 20)) # should return 5
import unittest

class Test(unittest.TestCase):
    def test_fruit_distribution(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
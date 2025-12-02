def fruit_distribution(s, n):
    total_fruits_list = [int(i) for i in s.split() if i.isdigit()]
    total_fruits = total_fruits_list[0] + total_fruits_list[1]
    mango_fruits = n - total_fruits_list[0] - total_fruits_list[1]
    return mango_fruits
import unittest

class Test(unittest.TestCase):
    def test_fruit_distribution(self):
        self.assertEqual(fruit_distribution("5 apples and 6 oranges", 19), 8)
        self.assertEqual(fruit_distribution("0 apples and 1 oranges", 3), 2)
        self.assertEqual(fruit_distribution("2 apples and 3 oranges", 100), 95)
        self.assertEqual(fruit_distribution("100 apples and 1 oranges", 120), 19)

if __name__ == '__main__':
    unittest.main()
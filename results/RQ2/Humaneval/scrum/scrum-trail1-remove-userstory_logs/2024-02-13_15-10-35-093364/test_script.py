def fruit_distribution(s, n):
    input_list = s.split()
    if len(input_list) != 4 or input_list[2] != 'and' or not input_list[0].isdigit() or not input_list[3].isdigit() or input_list[1] != 'apples' or input_list[3] != 'oranges':
        return 'Incorrect input string format. Please provide a valid input string.'
    apples = int(input_list[0])
    oranges = int(input_list[3])
    if n < (apples + oranges):
        return 'Total number of fruits is less than the sum of apples and oranges. Please provide a valid total number of fruits.'
    mango_fruits = n - apples - oranges
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
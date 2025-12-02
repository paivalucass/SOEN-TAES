def max_element(numbers: list) -> int:
    if not numbers:
        return "Error: Empty list"
    max_element = numbers[0]
    for num in numbers[1:]:
        if num > max_element:
            max_element = num
    return max_element
import unittest

class Test(unittest.TestCase):

    def test_max_element(self):
        self.assertEqual(max_element([1, 2, 3]), 3)
        self.assertEqual(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), 123)

if __name__ == '__main__':
    unittest.main()
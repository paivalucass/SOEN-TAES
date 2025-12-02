def median_numbers(a, b, c):
    numbers = [a, b, c]
    sorted_numbers = sorted(numbers)
    if not all(isinstance(num, (int, float)) for num in numbers):
        return "Invalid Input"
    else:
        return sorted_numbers[1] if len(set(numbers)) == 3 else sorted_numbers[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(median_numbers(25, 55, 65), 55.0)

if __name__ == '__main__':
    unittest.main()
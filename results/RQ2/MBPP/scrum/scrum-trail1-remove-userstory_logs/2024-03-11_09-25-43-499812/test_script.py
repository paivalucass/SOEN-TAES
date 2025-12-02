def second_smallest(numbers):
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")

    sorted_numbers = sorted(set(numbers))
    if len(sorted_numbers) < 2:
        raise ValueError("Input list must contain at least two unique numbers")

    return sorted_numbers[1]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()
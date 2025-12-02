def second_smallest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two numbers")

    min_num = float('inf')
    second_min = float('inf')
    for num in numbers:
        if num < min_num:
            second_min = min_num
            min_num = num
        elif num < second_min and num != min_num:
            second_min = num
    return second_min
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(second_smallest([1, 2, -8, -2, 0, -2]), -2)

if __name__ == '__main__':
    unittest.main()
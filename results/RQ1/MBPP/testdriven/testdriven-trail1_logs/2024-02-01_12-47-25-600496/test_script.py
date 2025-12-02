def cube_nums(input_numbers):
    if not input_numbers:
        return "Error: Empty input list"
    cubed_numbers = []
    for number in input_numbers:
        if isinstance(number, (int, float)):
            cubed_numbers.append(number ** 3)
        else:
            return "Error: Non-numeric values in input list"
    return cubed_numbers
import unittest

class Test(unittest.TestCase):
    def test_cube_nums(self):
        self.assertEqual(cube_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000])

if __name__ == '__main__':
    unittest.main()
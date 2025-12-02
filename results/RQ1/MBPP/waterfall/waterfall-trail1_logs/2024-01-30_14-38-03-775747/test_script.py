def difference(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input"

    sum_of_cubes = n * (n + 1) // 2
    sum_of_cubes = sum_of_cubes ** 2

    sum_of_natural_numbers = n * (n + 1) // 2

    result = sum_of_cubes - sum_of_natural_numbers

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
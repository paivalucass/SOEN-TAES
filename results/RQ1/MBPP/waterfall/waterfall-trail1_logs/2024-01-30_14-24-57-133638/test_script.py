def find_average_of_cube(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input parameter n must be a positive integer."

    if n == 0:
        return 0
    elif n == 1:
        return 1

    sum_cubes = sum(i**3 for i in range(1, n+1))
    average = sum_cubes / n
    return round(average, 2)

# Test case
assert find_average_of_cube(2) == 4.5
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
def find_Average_Of_Cube(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input 'n' must be a positive integer")

    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    average = sum_of_cubes / n
    return round(average, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
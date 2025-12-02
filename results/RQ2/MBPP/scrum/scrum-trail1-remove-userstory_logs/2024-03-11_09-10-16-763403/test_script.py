def find_Average_Of_Cube(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input should be a positive integer")

    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i**3

    average = sum_of_cubes / n
    return float(average)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
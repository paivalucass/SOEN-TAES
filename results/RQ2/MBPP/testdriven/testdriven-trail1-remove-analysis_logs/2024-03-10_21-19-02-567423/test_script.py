def find_Average_Of_Cube(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input"
    sum_cubes = 0
    for i in range(1, n+1):
        sum_cubes += i**3
    if n == 1:
        return 1.0
    average = sum_cubes / n
    return round(average, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
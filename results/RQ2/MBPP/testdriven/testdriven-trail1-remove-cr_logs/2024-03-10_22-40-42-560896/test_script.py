def find_Average_Of_Cube(n):
    """
    Write a python function to find the average of cubes of first n natural numbers.
    """
    if not isinstance(n, int) or n <= 0:
        return "Invalid input"
    
    sum_of_cubes = 0
    for i in range(1, n+1):
        sum_of_cubes += i**3
    
    average = sum_of_cubes / n
    return round(average, 10)  # Rounding to 10 decimal places

assert find_Average_Of_Cube(2) == 4.5
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
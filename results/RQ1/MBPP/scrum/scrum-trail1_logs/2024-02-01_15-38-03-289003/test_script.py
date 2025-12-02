def find_Average_Of_Cube(n):
    if n <= 0:
        return "Invalid input. Please enter a positive number for n."
    sum_of_cubes = sum(i*i*i for i in range(1, n+1))
    average = sum_of_cubes / n
    return average
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
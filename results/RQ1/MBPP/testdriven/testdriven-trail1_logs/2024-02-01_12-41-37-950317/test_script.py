def find_Average_Of_Cube(n):
    '''Write a python function to find the average of cubes of first n natural numbers.'''
    if not isinstance(n, int) or n <= 0:
        return "Invalid Input"

    cubes = [i**3 for i in range(1, n+1)]
    average = sum(cubes) / n
    return round(average, 2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
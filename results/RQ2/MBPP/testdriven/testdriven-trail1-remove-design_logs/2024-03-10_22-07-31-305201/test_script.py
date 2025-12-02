def find_Average_Of_Cube(n):
    if n <= 0:
        return "error"
    else:
        sum_of_cubes = 0
        for i in range(1, n+1):
            sum_of_cubes += i**3
        return sum_of_cubes / n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
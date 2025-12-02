def find_Average_Of_Cube(n):
    if n <= 0:
        return 0
    cubes = [i**3 for i in range(1, n+1)]
    average = sum(cubes) / n
    return average
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Average_Of_Cube(2), 4.5)

if __name__ == '__main__':
    unittest.main()
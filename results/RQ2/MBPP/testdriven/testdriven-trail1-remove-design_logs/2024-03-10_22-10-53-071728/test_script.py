def difference(n):
    sum_of_squares = (n * (n + 1) / 2) ** 2
    sum_of_cubes = (n * (n + 1) / 2) * (n * (n + 1) / 2)
    return sum_of_cubes - sum_of_squares
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
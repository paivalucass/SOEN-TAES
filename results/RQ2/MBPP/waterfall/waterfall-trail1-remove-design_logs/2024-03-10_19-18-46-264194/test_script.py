def difference(n):
    sum_of_cubes = 0
    sum_of_numbers = 0
    if isinstance(n, int) and n > 0:
        for i in range(1, n + 1):
            sum_of_cubes += i**3
            sum_of_numbers += i
        return (sum_of_cubes - (sum_of_numbers)**2)
    else:
        return "Invalid input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
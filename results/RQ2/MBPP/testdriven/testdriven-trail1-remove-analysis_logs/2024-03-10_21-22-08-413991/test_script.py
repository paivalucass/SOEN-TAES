def difference(n):
    if n == 0:
        return 0
    if not isinstance(n, int) or n < 0:
        return "Invalid input"
    
    sum_of_cubes = (n * (n + 1) // 2) ** 2
    sum_of_natural_numbers = (n * (n + 1)) // 2
    return sum_of_cubes - sum_of_natural_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
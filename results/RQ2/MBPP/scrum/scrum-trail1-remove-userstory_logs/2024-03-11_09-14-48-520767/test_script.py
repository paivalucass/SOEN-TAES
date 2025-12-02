def difference(n):
    if n <= 0 or type(n) is not int:
        raise ValueError("Input must be a positive integer")
    
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_natural_numbers = n * (n + 1) // 2
    return sum_of_cubes - sum_of_natural_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
def difference(n):
    try:
        if type(n) != int or n < 0:
            raise ValueError("Input must be a non-negative integer")
        
        sum_of_cubes = 0
        sum_of_natural_numbers = 0
        for i in range(1, n+1):
            sum_of_cubes += i**3
            sum_of_natural_numbers += i
        
        return sum_of_cubes - sum_of_natural_numbers
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
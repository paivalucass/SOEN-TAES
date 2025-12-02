def difference(n):
    if not isinstance(n, int):
        return "Input validation error"
    
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = sum(range(1, n+1))
    
    return sum_of_cubes - sum_of_numbers
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
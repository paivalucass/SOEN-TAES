def difference(n):
    if n <= 0:
        return "Invalid input: n should be a positive integer"
    
    sum_cubes = sum(i**3 for i in range(1, n+1))
    sum_natural = n * (n + 1) // 2
    
    return sum_cubes - sum_natural

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(difference(3), 30)

if __name__ == '__main__':
    unittest.main()
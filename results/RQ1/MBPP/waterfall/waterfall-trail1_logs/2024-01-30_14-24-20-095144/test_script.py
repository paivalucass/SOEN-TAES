def cube_Sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")

    cube_sum = 0
    for i in range(1, n+1):
        cube_sum += (2*i)**3
    return cube_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
def cube_Sum(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input should be a positive integer")

    cube_sum = sum([i ** 3 for i in range(2, 2*n+1, 2)])

    return cube_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
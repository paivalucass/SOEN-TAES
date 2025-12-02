def cube_Sum(n):
    total_cube_sum = 0
    for i in range(1, n*2 + 1):
        total_cube_sum += (i*2)**3
    return total_cube_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
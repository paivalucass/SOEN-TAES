def cube_Sum(n):
    total_sum = 0
    for i in range(2, (n*2)+2, 2):
        total_sum += (i**3)
    return total_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
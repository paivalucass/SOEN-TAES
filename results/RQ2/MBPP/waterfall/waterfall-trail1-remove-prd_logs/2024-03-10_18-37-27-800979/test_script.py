def cube_Sum(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    even_numbers = [i for i in range(2, n * 2 + 1, 2)]
    cube_sum = sum([i ** 3 for i in even_numbers])
    return cube_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
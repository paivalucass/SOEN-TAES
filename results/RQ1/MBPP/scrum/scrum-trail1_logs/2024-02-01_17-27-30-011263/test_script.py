def cube_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Invalid input"

    even_numbers = [i*2 for i in range(1, n+1)]
    cube_sum = sum([x**3 for x in even_numbers])

    return cube_sum
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
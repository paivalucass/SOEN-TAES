def cube_Sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Invalid input. Please provide a positive integer."

    result = 0
    for i in range(2, 2*n+2, 2):
        result += i*i*i

    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
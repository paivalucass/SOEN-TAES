def cube_Sum(n):
    result = 0
    for i in range(1, n+1):
        result += (2*i)**3
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(cube_Sum(2), 72)

if __name__ == '__main__':
    unittest.main()
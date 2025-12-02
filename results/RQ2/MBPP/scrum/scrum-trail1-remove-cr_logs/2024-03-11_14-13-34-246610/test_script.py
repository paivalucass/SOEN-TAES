def adjac(ele, sub = []):
    x, y = ele
    return [[x+i, y+j] for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()
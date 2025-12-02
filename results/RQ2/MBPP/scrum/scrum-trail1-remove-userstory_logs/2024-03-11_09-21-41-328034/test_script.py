def adjac(ele, sub=[]):
    adjacent_coords = []
    for i in range(ele[0]-1, ele[0]+2):
        for j in range(ele[1]-1, ele[1]+2):
            if (i, j) != ele:
                adjacent_coords.append([i, j])
    return adjacent_coords
import unittest

class Test(unittest.TestCase):
    def test_adjac(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()
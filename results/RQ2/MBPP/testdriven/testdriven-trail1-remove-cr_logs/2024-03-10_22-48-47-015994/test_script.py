def adjac(ele):
    x, y = ele
    adjacency_list = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i, j) != ele:
                adjacency_list.append([i, j])
    return adjacency_list
import unittest

class Test(unittest.TestCase):
    def test_adjac(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()
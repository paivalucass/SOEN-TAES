def adjac(ele, sub = []):
    # Write a function to extract all the adjacent coordinates of the given coordinate tuple.
    return [[ele[0]-1, ele[1]-1], [ele[0]-1, ele[1]], [ele[0]-1, ele[1]+1], 
            [ele[0], ele[1]-1], [ele[0], ele[1]], [ele[0], ele[1]+1],
            [ele[0]+1, ele[1]-1], [ele[0]+1, ele[1]], [ele[0]+1, ele[1]+1]]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()
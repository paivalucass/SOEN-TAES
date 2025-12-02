def adjac(ele, sub = []):
    result = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            result.append([ele[0]+i, ele[1]+j])
    result.remove(ele)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(adjac((3, 4)), [[2, 3], [2, 4], [2, 5], [3, 3], [3, 4], [3, 5], [4, 3], [4, 4], [4, 5]])

if __name__ == '__main__':
    unittest.main()
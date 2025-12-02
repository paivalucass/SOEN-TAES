def sort_matrix(M):
    if not M or len(M) == 1:
        return M

    M.sort(key=lambda x: sum(x))
    return M
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()
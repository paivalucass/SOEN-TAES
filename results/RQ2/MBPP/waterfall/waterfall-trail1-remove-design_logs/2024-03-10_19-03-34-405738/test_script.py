def sort_matrix(M):
    return sorted(M, key=lambda row: sum(row))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_matrix([[1, 2, 3], [2, 4, 5], [1, 1, 1]]), [[1, 1, 1], [1, 2, 3], [2, 4, 5]])

if __name__ == '__main__':
    unittest.main()
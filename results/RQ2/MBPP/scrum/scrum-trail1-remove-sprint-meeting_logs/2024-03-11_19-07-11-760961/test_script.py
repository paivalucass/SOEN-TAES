def extract_index_list(l1, l2, l3):
    result = [l1[i] for i in range(min(len(l1), len(l2), len(l3))) if l1[i] == l2[i] == l3[i]]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()
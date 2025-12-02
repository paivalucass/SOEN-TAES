def extract_index_list(l1, l2, l3):
    if len(set(map(len, (l1, l2, l3)))) != 1:
        return "Input lists are not of the same length"

    result = [x for x, y, z in zip(l1, l2, l3) if x == y == z]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()
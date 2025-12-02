def extract_index_list(l1, l2, l3):
    common_elements = [elem1 for (elem1, elem2, elem3) in zip(l1, l2, l3) if elem1 == elem2 == elem3]
    return common_elements
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_index_list([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]), [1, 7])

if __name__ == '__main__':
    unittest.main()
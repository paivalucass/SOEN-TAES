def similar_elements(test_tup1, test_tup2):
    if not isinstance(test_tup1, tuple) or not isinstance(test_tup2, tuple):
        return "Error"
    if len(test_tup1) == 0 and len(test_tup2) == 0:
        return "Both input tuples are empty"
    return set(test_tup1) & set(test_tup2)
import unittest

class Test(unittest.TestCase):
    def test_similar_elements(self):
        self.assertEqual(set(similar_elements((3, 4, 5, 6), (5, 7, 4, 10))), set((4, 5)))

if __name__ == '__main__':
    unittest.main()
def similar_elements(test_tup1, test_tup2):
    if not all(isinstance(item, (int, float)) for item in test_tup1) or not all(isinstance(item, (int, float)) for item in test_tup2):
        return TypeError
    return list(set(test_tup1) & set(test_tup2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)), [4, 5])

if __name__ == '__main__':
    unittest.main()
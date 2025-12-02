def similar_elements(test_tup1, test_tup2):
    return set(test_tup1) & set(test_tup2)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)), {4, 5})

if __name__ == '__main__':
    unittest.main()
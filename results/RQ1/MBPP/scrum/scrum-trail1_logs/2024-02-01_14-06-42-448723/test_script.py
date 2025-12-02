def similar_elements(test_list1, test_list2):
    if not isinstance(test_list1, list) or not isinstance(test_list2, list):
        raise TypeError('Input parameters must be lists')
    return list(set(test_list1) & set(test_list2))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(similar_elements((3, 4, 5, 6),(5, 7, 4, 10)), {4, 5})

if __name__ == '__main__':
    unittest.main()
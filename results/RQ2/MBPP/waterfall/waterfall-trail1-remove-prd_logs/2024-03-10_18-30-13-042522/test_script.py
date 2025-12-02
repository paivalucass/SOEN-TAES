def find_lists(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise TypeError("Input must be a tuple")
    
    list_count = sum(1 for element in input_tuple if isinstance(element, list))
    
    return list_count
import unittest

class Test(unittest.TestCase):
    def test_find_lists(self):
        self.assertEqual(find_lists(([1, 2, 3, 4], [5, 6, 7, 8])), 2)

if __name__ == '__main__':
    unittest.main()
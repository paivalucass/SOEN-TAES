def count_first_elements(test_tup: tuple) -> int:
    if len(test_tup) == 0:
        return "Error: Input tuple is empty"
    
    index_dict = {}
    for i in range(len(test_tup)):
        index_dict[test_tup[i]] = i
    
    if isinstance(test_tup[3], tuple):
        return index_dict[test_tup[3]]
    else:
        return "Error: Tuple element does not exist in the input tuple"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_first_elements((1, 5, 7, (4, 6), 10)), 3)

if __name__ == '__main__':
    unittest.main()
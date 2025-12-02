def check_occurrences(test_list):
    if not test_list:
        raise ValueError("Input list is empty")
    
    occurrences_count = {}
    for tuple_item in test_list:
        if not isinstance(tuple_item, tuple):
            raise ValueError("Input list contains non-tuple elements")
        
        if tuple_item in occurrences_count:
            occurrences_count[tuple_item] += 1
        else:
            occurrences_count[tuple_item] = 1
    
    return occurrences_count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]), {(3, 1): 1, (1, 3): 1, (2, 5): 1, (5, 2): 1, (6, 3): 1})

if __name__ == '__main__':
    unittest.main()
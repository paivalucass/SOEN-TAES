def index_minimum(test_list):
    if not isinstance(test_list, list) or not all(isinstance(tup, tuple) and len(tup) == 2 for tup in test_list):
        raise ValueError("Invalid input data: input must be a list of tuples with length 2")
    
    if not test_list:
        return None  # handle empty input list
    
    min_tuple = test_list[0]
    for tup in test_list:
        if tup[1] < min_tuple[1]:
            min_tuple = tup
    return min_tuple[0]
import unittest

class Test(unittest.TestCase):
    def test_index_minimum(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()
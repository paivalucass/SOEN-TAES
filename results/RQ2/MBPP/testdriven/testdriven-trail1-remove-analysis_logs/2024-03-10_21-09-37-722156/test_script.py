def index_minimum(test_list):
    '''
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
    '''
    if not isinstance(test_list, list):
        return "Error: Input is not a list"
    
    for item in test_list:
        if not isinstance(item, tuple) or len(item) != 2:
            return "Error: Input format is incorrect"
    
    min_value = float('inf')
    result = None
    for item in test_list:
        if item[1] < min_value:
            min_value = item[1]
            result = item[0]
    return result
import unittest

class Test(unittest.TestCase):
    def test_index_minimum(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()
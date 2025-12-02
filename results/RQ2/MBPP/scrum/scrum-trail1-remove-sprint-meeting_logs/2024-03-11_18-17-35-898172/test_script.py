def index_minimum(test_list):
    if not test_list or not all(isinstance(item, tuple) and len(item) == 2 for item in test_list):
        raise ValueError("Invalid input. Please provide a non-empty list of tuples with two elements each.")
    
    min_second_value = float('inf')
    result = None
    
    for name, value in test_list:
        if value < min_second_value:
            min_second_value = value
            result = name
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()
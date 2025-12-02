def index_minimum(test_list):
    if not test_list or not all(isinstance(item, tuple) and len(item) == 2 and isinstance(item[1], int) for item in test_list):
        return "Error: Invalid input format"
    
    min_tuple = min(test_list, key=lambda x: x[1])
    return min_tuple[0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()
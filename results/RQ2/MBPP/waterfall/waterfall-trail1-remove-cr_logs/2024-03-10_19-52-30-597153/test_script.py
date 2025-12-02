def index_minimum(test_list):
    import heapq
    
    try:
        if not test_list:
            raise ValueError("Error: Empty input list")
        
        min_second_val_tuple = heapq.nsmallest(1, test_list, key=lambda x: x[1])[0]
        return min_second_val_tuple[0]
    
    except IndexError:
        raise ValueError("Invalid second values in input tuples")
import unittest

class Test(unittest.TestCase):
    def test_index_minimum(self):
        self.assertEqual(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]), 'Varsha')

if __name__ == '__main__':
    unittest.main()
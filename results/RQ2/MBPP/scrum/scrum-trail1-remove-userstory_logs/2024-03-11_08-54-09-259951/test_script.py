def sort_sublists(input_list):
    modified_list = [sublist[:] for sublist in input_list]
    
    for sublist in modified_list:
        sublist.sort()
    
    return modified_list
import unittest

class Test(unittest.TestCase):
    def test_sort_sublists(self):
        self.assertEqual(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()
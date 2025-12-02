def sort_sublists(input_list):
    if not all(isinstance(sublist, list) for sublist in input_list):
        raise ValueError("Input_list must be a list of lists")

    sorted_list = []
    for sublist in input_list:
        sorted_sublist = sorted(sublist)
        sorted_list.append(sorted_sublist)
    
    return sorted_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()
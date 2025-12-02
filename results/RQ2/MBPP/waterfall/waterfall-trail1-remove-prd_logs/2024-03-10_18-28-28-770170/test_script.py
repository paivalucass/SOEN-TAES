def sort_sublists(input_list):
    for sublist in input_list:
        if isinstance(sublist, list):
            sublist.sort()
        else:
            pass  # Handle non-list elements in a specific way
    return input_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()
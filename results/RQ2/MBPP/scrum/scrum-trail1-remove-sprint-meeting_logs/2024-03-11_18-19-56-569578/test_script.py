def sort_sublists(input_list):
    sorted_input_list = [sorted(sublist) for sublist in input_list]
    return sorted_input_list

assert sort_sublists(([], ['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']))==[[], ['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]
assert sort_sublists([[3, 2, 1], [6, 5, 4], [9, 8, 7], [-3, -2, -1]])==[[1, 2, 3], [4, 5, 6], [7, 8, 9], [-3, -2, -1]]
import unittest

class Test(unittest.TestCase):
    def test_sort_sublists(self):
        self.assertEqual(sort_sublists([["green", "orange"], ["black", "white"], ["white", "black", "orange"]]), [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']])

if __name__ == '__main__':
    unittest.main()
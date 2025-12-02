def unique_sublists(input_list):
    unique_sublists_count = {}
    if not isinstance(input_list, list):
        raise ValueError("Input must be a list")
    for sublist in input_list:
        if not isinstance(sublist, list):
            raise ValueError("Input must be a list of lists")
        tuple_sublist = tuple(sublist)
        if tuple_sublist in unique_sublists_count:
            unique_sublists_count[tuple_sublist] += 1
        else:
            unique_sublists_count[tuple_sublist] = 1
    return unique_sublists_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()
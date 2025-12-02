def group_tuples(input_list):
    grouped_dict = {}
    for tuple_ in input_list:
        common_first_element = tuple_[0]
        if common_first_element in grouped_dict:
            grouped_dict[common_first_element].append(tuple_[1])
        else:
            grouped_dict[common_first_element] = [tuple_[1]]
    grouped_list = [(key,) + tuple(val) for key, val in grouped_dict.items()]
    return grouped_list
import unittest

class Test(unittest.TestCase):
    def test_group_tuples(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
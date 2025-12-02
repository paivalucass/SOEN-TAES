def group_tuples(input_list):
    result_dict = {}
    for tup in input_list:
        if tup[0] in result_dict:
            result_dict[tup[0]].append(tup[1])
        else:
            result_dict[tup[0]] = [tup[1]]
    result_list = [(key, *value) for key, value in result_dict.items()]
    return result_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
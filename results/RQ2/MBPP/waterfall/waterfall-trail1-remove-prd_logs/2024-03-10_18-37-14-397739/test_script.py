def group_tuples(list_of_tuples):
    if not isinstance(list_of_tuples, list):
        raise TypeError("Input must be a list of tuples")
    grouped_dict = {}
    for item in list_of_tuples:
        if item[0] in grouped_dict:
            grouped_dict[item[0]].append(item[1])
        else:
            grouped_dict[item[0]] = [item[1]]

    grouped_tuples = [(key, *value) for key, value in grouped_dict.items()]

    return grouped_tuples
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
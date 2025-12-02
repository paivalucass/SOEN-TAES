def group_tuples(Input):
    grouped_dict = {}
    for item in Input:
        key = item[0]
        if key in grouped_dict:
            grouped_dict[key].append(item)
        else:
            grouped_dict[key] = [item]
    
    result = []
    for key, value in grouped_dict.items():
        new_tuple = (key,) + tuple([element for sublist in value for element in sublist[1:]])
        result.append(new_tuple)
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
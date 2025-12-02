def group_tuples(input_list):
    result = {}
    for tpl in input_list:
        key = tpl[0]
        value = tpl[1]
        if key in result:
            result[key].append(value)
        else:
            result[key] = [value]
    final_result = [(key, *values) for key, values in result.items()]
    return final_result

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
def group_tuples(Input):
    result_dict = {}
    for i in Input:
        if i[0] in result_dict:
            result_dict[i[0]].append(i[1])
        else:
            result_dict[i[0]] = [i[1]]
    result = [(key, *value) for key, value in result_dict.items()]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
def group_tuples(Input):
    from collections import defaultdict
    output = defaultdict(list)
    for item in Input:
        output[item[0]].append(item[1])
    result = [(key, *value) for key, value in output.items()]
    return result
import unittest

class Test(unittest.TestCase):
    def test_group_tuples(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
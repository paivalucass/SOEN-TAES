def group_tuples(Input):
    from collections import defaultdict

    result = defaultdict(list)

    for item in Input:
        key = item[0]
        result[key].append(item[1])

    final_result = [(key, *value) for key, value in result.items()]

    return final_result
import unittest

class Test(unittest.TestCase):
    def test_group_tuples(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
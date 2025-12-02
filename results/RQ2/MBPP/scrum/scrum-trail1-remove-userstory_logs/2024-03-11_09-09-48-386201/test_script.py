def group_tuples(Input):
    if not Input:
        return []

    grouped = {}
    for tpl in Input:
        key = tpl[0]
        if key in grouped:
            grouped[key].append(tpl[1])
        else:
            grouped[key] = [tpl[1]]

    result = [(key, *values) for key, values in grouped.items()]

    return result
import unittest

class Test(unittest.TestCase):
    def test_group_tuples(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
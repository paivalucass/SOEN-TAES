def group_tuples(Input):
    from collections import defaultdict
    
    common_first_elements = defaultdict(list)
    for item in Input:
        common_first_elements[item[0]].append(item[1])
    
    result = [tuple([k] + v) for k, v in common_first_elements.items() if len(v) > 1]
    return result

import unittest

class Test(unittest.TestCase):
    def test_group_tuples(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
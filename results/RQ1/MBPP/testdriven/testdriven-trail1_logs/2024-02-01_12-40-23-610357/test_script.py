from collections import defaultdict

def group_tuples(Input):
    common_elements = defaultdict(list)
    
    for tup in Input:
        common_elements[tup[0]].append(tup[1])
    
    res = []
    
    for val in common_elements.values():
        if len(val) > 1:
            new_tup = (val[0],) + tuple(val[1:])
            res.append(new_tup)
    
    return res

import unittest

class Test(unittest.TestCase):
    def test_group_tuples(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
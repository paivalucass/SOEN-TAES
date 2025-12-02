def group_tuples(Input):
    from collections import defaultdict
    
    hash_map = defaultdict(list)
    
    for tpl in Input:
        key = tpl[0]
        hash_map[key].append(tpl[1])
    
    result = []
    
    for key in hash_map:
        group = [key] + hash_map[key]
        result.append(tuple(group))
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
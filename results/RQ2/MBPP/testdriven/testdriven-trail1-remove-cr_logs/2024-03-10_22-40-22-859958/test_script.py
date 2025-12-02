def group_tuples(Input):
    from collections import defaultdict
    
    grouped_tuples = defaultdict(list)
    
    for tup in Input:
        grouped_tuples[tup[0]].extend(tup[1:])
    
    result = [tuple([key] + val) for key, val in grouped_tuples.items()]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(group_tuples([('x', 'y'), ('x', 'z'), ('w', 't')]), [('x', 'y', 'z'), ('w', 't')])

if __name__ == '__main__':
    unittest.main()
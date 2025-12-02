def unique_sublists(list1):
    from collections import defaultdict
    
    if not isinstance(list1, list):
        return "Error: Input is not a list"
    
    result = defaultdict(int)
    for l in list1:
        key = tuple(l)
        result[key] += 1
    
    return dict(result)
import unittest

class Test(unittest.TestCase):
    def test_unique_sublists(self):
        self.assertEqual(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]), {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1})

if __name__ == '__main__':
    unittest.main()
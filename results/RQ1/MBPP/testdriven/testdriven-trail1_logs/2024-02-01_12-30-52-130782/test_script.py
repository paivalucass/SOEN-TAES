def dict_depth(d, depth=1):
    '''Write a function to find the depth of a dictionary.'''
    if not isinstance(d, dict) or not d:
        return depth - 1
    max_depth = depth
    for key, value in d.items():
        if isinstance(value, dict):
            max_depth = max(max_depth, dict_depth(value, depth + 1))
    return max_depth
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
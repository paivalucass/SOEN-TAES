def dict_depth(d, depth=1):
    if not isinstance(d, dict):
        raise ValueError("Input is not a dictionary")
    if not d:
        return depth
    return max(dict_depth(val, depth+1) for val in d.values() if isinstance(val, dict))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a': 1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
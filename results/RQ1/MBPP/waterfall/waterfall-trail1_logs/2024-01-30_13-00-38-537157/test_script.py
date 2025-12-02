def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 0
    return 1 + max(dict_depth(val) for val in d.values() if isinstance(val, dict))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
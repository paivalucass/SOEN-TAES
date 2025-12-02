def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1
    return 1 + max(dict_depth(d[key]) for key in d)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
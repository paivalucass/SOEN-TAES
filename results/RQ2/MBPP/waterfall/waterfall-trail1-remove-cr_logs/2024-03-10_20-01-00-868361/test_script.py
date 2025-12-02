def dict_depth(d):
    max_depth = 1
    if isinstance(d, dict):
        for key, value in d.items():
            if isinstance(value, dict):
                max_depth = max(max_depth, 1 + dict_depth(value))
    return max_depth
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
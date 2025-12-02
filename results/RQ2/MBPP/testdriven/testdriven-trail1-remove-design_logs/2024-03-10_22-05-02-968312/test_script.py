def dict_depth(d, depth=1):
    if not isinstance(d, dict) or not d:
        return 0
    if all(isinstance(v, dict) for v in d.values()):
        return depth
    return max(dict_depth(v, depth + 1) for v in d.values() if isinstance(v, dict))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
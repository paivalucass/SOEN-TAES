def dict_depth(d):
    if not isinstance(d, dict):
        raise TypeError("Input is not a dictionary")

    depth = 1
    for key, value in d.items():
        if isinstance(value, dict):
            new_depth = 1 + dict_depth(value)
            depth = max(depth, new_depth)

    return depth
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
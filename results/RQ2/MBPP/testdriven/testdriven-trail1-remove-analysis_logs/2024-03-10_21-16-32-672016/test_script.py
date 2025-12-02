def dict_depth(d):
    depth = 0
    if not isinstance(d, dict) or not d:
        return depth
    queue = [(d, 1)]
    while queue:
        current, current_depth = queue.pop(0)
        depth = max(depth, current_depth)
        for k, v in current.items():
            if isinstance(v, dict):
                queue.append((v, current_depth + 1))
    return depth
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
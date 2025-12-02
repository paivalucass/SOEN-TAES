def dict_depth(d):
    stack = [(d, 1)]
    max_depth = 0

    while stack:
        current_dict, depth = stack.pop()
        if depth > max_depth:
            max_depth = depth

        for key, value in current_dict.items():
            if isinstance(value, dict):
                stack.append((value, depth + 1))

    return max_depth
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(dict_depth({'a':1, 'b': {'c': {'d': {}}}}), 4)

if __name__ == '__main__':
    unittest.main()
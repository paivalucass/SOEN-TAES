def drop_empty(dict1):
    if not isinstance(dict1, dict):
        raise ValueError("Input must be a dictionary")

    if any(not isinstance(key, str) for key in dict1.keys()):
        raise ValueError("Dictionary keys must be strings")

    return {key: value for key, value in dict1.items() if value is not None}
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3': None}), {'c1': 'Red', 'c2': 'Green'})

if __name__ == '__main__':
    unittest.main()
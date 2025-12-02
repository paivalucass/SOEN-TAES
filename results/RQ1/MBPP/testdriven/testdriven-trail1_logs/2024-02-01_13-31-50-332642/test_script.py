def return_sum(dict):
    # Write function to find the sum of all items in the given dictionary.
    if not dict:
        raise ValueError("Input dictionary is empty")
    if not all(isinstance(value, (int, float)) for value in dict.values()):
        raise ValueError("Input dictionary should contain only numeric values")
    return sum(dict.values())
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(return_sum({'a': 100, 'b':200, 'c':300}), 600)

if __name__ == '__main__':
    unittest.main()
def merge(lst):
    if not all(isinstance(sublist, list) and len(sublist) == 2 for sublist in lst):
        return "Error: Invalid input type"

    transposed_list = [[sub[0] for sub in lst], [sub[1] for sub in lst]]
    return transposed_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()
def merge(lst):
    if not lst:
        return "Error Message: Input list is empty"
    for sublist in lst:
        if len(sublist) != 2:
            return "Error Message: Sublists must have exactly two elements"
    result = [[sublist[0] for sublist in lst], [sublist[1] for sublist in lst]]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()
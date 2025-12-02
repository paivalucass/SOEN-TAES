def merge(lst):
    if not lst or any(len(sublist) != 2 for sublist in lst):
        raise ValueError("Input list should not be empty and sublists should have exactly two elements")
    return [list(x) for x in zip(*lst)]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()
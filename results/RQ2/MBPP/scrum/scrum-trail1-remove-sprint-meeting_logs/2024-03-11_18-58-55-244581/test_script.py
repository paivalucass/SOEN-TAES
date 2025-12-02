def merge(lst):
    return [list(x) for x in zip(*lst)]

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(merge([['x', 'y'], ['a', 'b'], ['m', 'n']]), [['x', 'a', 'm'], ['y', 'b', 'n']])

if __name__ == '__main__':
    unittest.main()
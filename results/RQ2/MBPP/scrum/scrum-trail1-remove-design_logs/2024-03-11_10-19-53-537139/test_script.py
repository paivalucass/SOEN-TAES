def combinations_colors(l, n):
    import itertools
    return list(itertools.product(l, repeat=n))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(combinations_colors(["Red","Green","Blue"], 1), [('Red',), ('Green',), ('Blue',)])

if __name__ == '__main__':
    unittest.main()
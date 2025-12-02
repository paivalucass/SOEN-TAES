def even_ele(test_tuple, even_fnc):
    def extract_even(t):
        if isinstance(t, tuple):
            return tuple(extract_even(i) for i in t if even_fnc(i))
        else:
            return t
    return extract_even(test_tuple)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
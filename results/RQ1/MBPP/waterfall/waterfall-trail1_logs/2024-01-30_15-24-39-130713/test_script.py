def even_ele(test_tuple, even_fnc):
    result = tuple(filter(even_fnc, test_tuple))
    return result

def extract_even(t):
    return even_ele(t, lambda x: isinstance(x, int) and x % 2 == 0)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
def even_ele(test_tuple, even_fnc):
    result = ()
    for item in test_tuple:
        if isinstance(item, tuple):
            result += (even_ele(item, even_fnc),)
        else:
            if even_fnc(item):
                result += (item,)
    return result
import unittest

class Test(unittest.TestCase):
    def test_even_ele(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
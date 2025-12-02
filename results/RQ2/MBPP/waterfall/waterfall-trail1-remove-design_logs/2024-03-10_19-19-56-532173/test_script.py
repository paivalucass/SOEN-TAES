def even_ele(test_tuple, even_fnc):
    result = []
    for elem in test_tuple:
        if isinstance(elem, tuple):
            result.append(even_ele(elem, even_fnc))
        elif isinstance(elem, int) and elem % 2 == 0:
            result.append(elem)
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
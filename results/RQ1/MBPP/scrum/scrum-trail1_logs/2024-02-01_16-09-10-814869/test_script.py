def even_ele(test_tuple, even_fnc):
    def remove_uneven_elements(tup, even_fnc):
        result = []
        for item in tup:
            if isinstance(item, tuple):
                result.append(remove_uneven_elements(item, even_fnc))
            else:
                if even_fnc(item):
                    result.append(item)
        return tuple(result)

    return remove_uneven_elements(test_tuple, even_fnc)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
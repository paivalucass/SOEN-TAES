def extract_even(test_tuple, even_fnc):
    result = []
    for item in test_tuple:
        if isinstance(item, tuple):
            result.append(extract_even(item, even_fnc))
        else:
            if even_fnc(item):
                result.append(item)
    return tuple(result)

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(extract_even((4, 5, (7, 6, (2, 4)), 6, 8)), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
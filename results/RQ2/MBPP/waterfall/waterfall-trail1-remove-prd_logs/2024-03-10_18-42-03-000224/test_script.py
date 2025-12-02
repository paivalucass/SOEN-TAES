def extract_even(test_tuple, even_fnc):
    result = []
    for item in test_tuple:
        if isinstance(item, tuple):
            nested_result = extract_even(item, even_fnc)
            if len(nested_result) > 0:
                result.append(nested_result)
        else:
            if isinstance(item, int) and even_fnc(item):
                result.append(item)
    return tuple(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
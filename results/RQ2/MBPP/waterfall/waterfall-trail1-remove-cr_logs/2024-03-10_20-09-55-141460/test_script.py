def extract_even(tpl, even_fnc):
    res = []
    for ele in tpl:
        if isinstance(ele, tuple):
            res.append(extract_even(ele, even_fnc))
        elif isinstance(ele, int) and even_fnc(ele):
            res.append(ele)
    return tuple(res)


def even_ele(test_tuple, even_fnc):
    return extract_even(test_tuple, even_fnc)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(even_ele((4, 5, (7, 6, (2, 4)), 6, 8), even_ele), (4, (6, (2, 4)), 6, 8))

if __name__ == '__main__':
    unittest.main()
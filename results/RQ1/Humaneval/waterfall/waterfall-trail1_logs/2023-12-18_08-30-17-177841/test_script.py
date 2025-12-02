def compare_one(a, b):
    def compare_integers(a, b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None

    def compare_floats(a, b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None

    def compare_strings(a, b):
        a = a.replace(',', '.')
        b = b.replace(',', '.')
        if float(a) > float(b):
            return a
        elif float(b) > float(a):
            return b
        else:
            return None

    try:
        if isinstance(a, int) and isinstance(b, int):
            return compare_integers(a, b)
        elif isinstance(a, float) and isinstance(b, float):
            return compare_floats(a, b)
        elif (isinstance(a, str) and isinstance(b, str)):
            return compare_strings(a, b)
        else:
            return None
    except (ValueError, TypeError):
        return None

import unittest

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == '__main__':
    unittest.main()
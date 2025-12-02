def compare_one(a, b):
    try:
        a = float(a.replace(",", ".")) if isinstance(a, str) else float(a)
        b = float(b.replace(",", ".")) if isinstance(b, str) else float(b)
    except ValueError:
        return None
    if a > b:
        return a if not isinstance(a, str) else str(a)
    elif b > a:
        return b if not isinstance(b, str) else str(b)
    else:
        return None

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == '__main__':
    unittest.main()
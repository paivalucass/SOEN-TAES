def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(',', '.') if ',' in a else float(a)
    if isinstance(b, str):
        b = b.replace(',', '.') if ',' in b else float(b)

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertEqual(compare_one("1", 1), None)

if __name__ == '__main__':
    unittest.main()
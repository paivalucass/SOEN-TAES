def compare_one(a, b):
    if isinstance(a, str):
        a = a.replace(',', '.')
    if isinstance(b, str):
        b = b.replace(',', '.')
    if float(a) == float(b):
        return None
    return max(float(a), float(b))
import unittest

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertEqual(compare_one("1", 1), None)

if __name__ == '__main__':
    unittest.main()
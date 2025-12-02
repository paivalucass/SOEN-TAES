def compare_one(a, b):
    a = str(a).replace(',', '.') if isinstance(a, str) else a
    b = str(b).replace(',', '.') if isinstance(b, str) else b
    if a == b:
        return None
    return max(a, b)
import unittest

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == '__main__':
    unittest.main()
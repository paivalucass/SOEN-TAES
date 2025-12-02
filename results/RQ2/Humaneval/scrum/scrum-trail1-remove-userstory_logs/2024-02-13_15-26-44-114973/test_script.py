def compare_one(a, b):
    if a == b:
        return None
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    if isinstance(a, str) and isinstance(b, str):
        a = a.replace(",", ".")
        b = b.replace(",", ".")
        return max(a, b)
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
def compare_one(a, b):
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return max(a, b) if a != b else None
    elif (isinstance(a, str) and any(char in a for char in [',', '.'])) and (isinstance(b, str) and any(char in b for char in [',', '.'])):
        a = a.replace(',', '.') if ',' in a else a
        b = b.replace(',', '.') if ',' in b else b
        return str(max(float(a), float(b)))
    else:
        raise ValueError("Invalid input types")
import unittest

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == '__main__':
    unittest.main()
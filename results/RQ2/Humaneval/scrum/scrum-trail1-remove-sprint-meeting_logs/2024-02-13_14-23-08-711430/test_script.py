def compare_one(a, b):
    if a == b:
        return None
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    else:
        a = str(a).replace(',', '.') if isinstance(a, str) else a
        b = str(b).replace(',', '.') if isinstance(b, str) else b
        return max(float(a), float(b))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertEqual(compare_one("1", 1), None)

if __name__ == '__main__':
    unittest.main()
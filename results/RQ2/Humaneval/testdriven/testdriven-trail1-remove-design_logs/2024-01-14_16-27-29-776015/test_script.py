def compare_one(a, b):
    if a == b:
        return None
    
    if isinstance(a, (int, float)):
        if isinstance(b, (int, float)):
            return max(a, b)
        elif isinstance(b, str):
            return handle_string_input(a, b)
    elif isinstance(a, str):
        if isinstance(b, (int, float)):
            return handle_string_input(b, a)
        elif isinstance(b, str):
            return handle_string_input(a, b)


def handle_string_input(a, b):
    a = a.replace(',', '.') if isinstance(a, str) else a
    b = b.replace(',', '.') if isinstance(b, str) else b
    return max(float(a), float(b))
import unittest

class Test(unittest.TestCase):
    def test_compare_one(self):
        self.assertEqual(compare_one(1, 2.5), 2.5)
        self.assertEqual(compare_one(1, "2,3"), "2,3")
        self.assertEqual(compare_one("5,1", "6"), "6")
        self.assertIsNone(compare_one("1", 1))

if __name__ == '__main__':
    unittest.main()